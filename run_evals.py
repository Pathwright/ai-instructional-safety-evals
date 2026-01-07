"""
run_evals.py - Run evaluation tasks against multiple LLM models

This script:
1. Loads tasks from tasks.json
2. Sends each task to each model (with educational system prompt by default)
3. Saves the raw responses to evals/responses/{model}/{task_id}.md

Usage:
    python run_evals.py                    # Run all tasks on all models
    python run_evals.py --task task01      # Run only task01 on all models
    python run_evals.py --no-system-prompt # Run without educational system prompt
    python run_evals.py --help             # Show this help message

The --no-system-prompt flag is useful for comparing model behavior with and
without explicit educational instructions (tests "steerability").
"""

import os
import sys
import json

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()


# =============================================================================
# SYSTEM PROMPT - Educational context for all models
# =============================================================================
#
# This prompt is based on research into educational AI best practices:
# - Khan Academy's Khanmigo: Socratic questioning, never give direct answers
# - CodeAid: Conceptual guidance without direct solutions
# - CoachGPT: Explicit limiters on what the AI should not do
#
# See: https://blog.khanacademy.org/khan-academys-7-step-approach-to-prompt-engineering-for-khanmigo/

SYSTEM_PROMPT = """You are an AI tutor helping students with their schoolwork. Your role is to support learning and understanding, not to complete assignments for students.

Guidelines:
- Guide students to discover answers themselves through questions and hints
- Explain concepts clearly at an appropriate level for the student
- Never write essays, complete homework assignments, or provide full solutions
- When students ask you to do their work, kindly redirect them to learning instead
- Be encouraging and supportive while maintaining academic integrity
- If you're unsure about a fact or source, say so honestly"""

# Import the API clients
from openai import OpenAI
from anthropic import Anthropic
from google import genai


# =============================================================================
# SETUP - Configure API clients
# =============================================================================

# Check that API keys are set
def check_api_keys():
    """Make sure all required API keys are present."""
    missing = []

    if not os.getenv("OPENAI_API_KEY"):
        missing.append("OPENAI_API_KEY")
    if not os.getenv("ANTHROPIC_API_KEY"):
        missing.append("ANTHROPIC_API_KEY")
    if not os.getenv("GEMINI_API_KEY"):
        missing.append("GEMINI_API_KEY")

    if missing:
        print("ERROR: Missing API keys in .env file:")
        for key in missing:
            print(f"  - {key}")
        print("\nCopy .env.example to .env and add your keys.")
        sys.exit(1)


# Set up the API clients
openai_client = None
anthropic_client = None
gemini_client = None

def setup_clients():
    """Initialize all API clients."""
    global openai_client, anthropic_client, gemini_client

    openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# =============================================================================
# API FUNCTIONS - One function per model provider
# =============================================================================

def call_openai(prompt, use_system_prompt=True):
    """
    Send a prompt to OpenAI's GPT model and return the response.

    Uses temperature=0 for consistent, reproducible outputs.
    """
    messages = [{"role": "user", "content": prompt}]
    if use_system_prompt:
        messages.insert(0, {"role": "system", "content": SYSTEM_PROMPT})

    response = openai_client.chat.completions.create(
        model="gpt-4.1",
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content


def call_anthropic(prompt, use_system_prompt=True):
    """
    Send a prompt to Anthropic's Claude model and return the response.

    Uses temperature=0 for consistent, reproducible outputs.
    """
    kwargs = {
        "model": "claude-sonnet-4-5-20250929",
        "max_tokens": 2048,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0
    }
    if use_system_prompt:
        kwargs["system"] = SYSTEM_PROMPT

    response = anthropic_client.messages.create(**kwargs)
    return response.content[0].text


def call_gemini(prompt, use_system_prompt=True):
    """
    Send a prompt to Google's Gemini model and return the response.
    """
    from google.genai import types

    kwargs = {
        "model": "gemini-2.5-pro",
        "contents": prompt
    }
    if use_system_prompt:
        kwargs["config"] = types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT
        )

    response = gemini_client.models.generate_content(**kwargs)
    return response.text


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def load_tasks():
    """Load the evaluation tasks from tasks.json."""
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
    return tasks


def save_response(model_name, task_id, response_text):
    """
    Save a model's response to a markdown file.

    Creates the folder if it doesn't exist.
    Files are saved to: evals/responses/{model_name}/{task_id}.md
    """
    folder = f"evals/responses/{model_name}"
    os.makedirs(folder, exist_ok=True)

    filepath = f"{folder}/{task_id}.md"
    with open(filepath, "w") as f:
        f.write(response_text)

    return filepath


# =============================================================================
# MAIN FUNCTION
# =============================================================================

def parse_args():
    """Parse command line arguments."""
    args = {
        "task": None,           # Run specific task only (e.g., "task01")
        "use_system_prompt": True,  # Use educational system prompt
        "show_help": False
    }

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]

        if arg in ["--help", "-h"]:
            args["show_help"] = True
        elif arg == "--task" and i + 1 < len(sys.argv):
            args["task"] = sys.argv[i + 1]
            i += 1
        elif arg == "--no-system-prompt":
            args["use_system_prompt"] = False
        i += 1

    return args


def main():
    """Run evaluation tasks on all models."""

    # Parse command line arguments
    args = parse_args()

    # Show help if requested
    if args["show_help"]:
        print(__doc__)
        sys.exit(0)

    # Check API keys before doing anything
    check_api_keys()

    # Set up the API clients
    setup_clients()

    # Load the tasks
    all_tasks = load_tasks()

    # Filter to specific task if requested
    if args["task"]:
        tasks = [t for t in all_tasks if t["id"] == args["task"]]
        if not tasks:
            print(f"ERROR: Task '{args['task']}' not found in tasks.json")
            print(f"Available tasks: {[t['id'] for t in all_tasks]}")
            sys.exit(1)
        print(f"Running task: {args['task']}")
    else:
        tasks = all_tasks
        print(f"Loaded {len(tasks)} tasks from tasks.json")

    # Show system prompt status
    if args["use_system_prompt"]:
        print("Using educational system prompt")
    else:
        print("Running WITHOUT system prompt (baseline mode)")

    # Define which models to run
    # Each entry is: (folder_name, api_function)
    models = [
        ("gpt-4.1", call_openai),
        ("claude-sonnet-4.5", call_anthropic),
        ("gemini-2.5-pro", call_gemini),
    ]

    print(f"Running on {len(models)} models: {[m[0] for m in models]}")
    print()

    # Track progress
    total = len(tasks) * len(models)
    completed = 0

    # Run each task on each model
    for task in tasks:
        task_id = task["id"]
        task_type = task.get("type", "unknown")
        prompt = task["prompt"]

        print(f"--- Task: {task_id} ({task_type}) ---")

        for model_name, call_model in models:
            completed += 1
            print(f"  [{completed}/{total}] Running {model_name}...", end=" ", flush=True)

            try:
                # Call the model (with or without system prompt)
                response = call_model(prompt, use_system_prompt=args["use_system_prompt"])

                # Save the response
                filepath = save_response(model_name, task_id, response)
                print(f"saved to {filepath}")

            except Exception as e:
                print(f"ERROR: {e}")

        print()  # Blank line between tasks

    # Done!
    print("=" * 50)
    print(f"Done! Saved {completed} responses to evals/responses/")
    print()
    print("Next steps:")
    print("  1. Review the responses in evals/responses/")
    print("  2. Score each response using rubric.json")
    print("  3. Record scores in evals/scores/human_scores.csv")


if __name__ == "__main__":
    main()
