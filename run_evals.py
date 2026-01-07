"""
run_evals.py - Run evaluation tasks against multiple LLM models

This script:
1. Loads tasks from tasks.json
2. Sends each task to each model
3. Saves the raw responses to evals/responses/{model}/{task_id}.md

Usage:
    python run_evals.py           # Run all tasks on all models
    python run_evals.py --help    # Show this help message
"""

import os
import sys
import json

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Import the API clients
from openai import OpenAI
from anthropic import Anthropic
import google.generativeai as genai


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
    if not os.getenv("GOOGLE_API_KEY"):
        missing.append("GOOGLE_API_KEY")

    if missing:
        print("ERROR: Missing API keys in .env file:")
        for key in missing:
            print(f"  - {key}")
        print("\nCopy .env.example to .env and add your keys.")
        sys.exit(1)


# Set up the API clients
openai_client = None
anthropic_client = None

def setup_clients():
    """Initialize all API clients."""
    global openai_client, anthropic_client

    openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# =============================================================================
# API FUNCTIONS - One function per model provider
# =============================================================================

def call_openai(prompt):
    """
    Send a prompt to OpenAI's GPT model and return the response.

    Uses temperature=0 for consistent, reproducible outputs.
    """
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content


def call_anthropic(prompt):
    """
    Send a prompt to Anthropic's Claude model and return the response.

    Uses temperature=0 for consistent, reproducible outputs.
    """
    response = anthropic_client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.content[0].text


def call_gemini(prompt):
    """
    Send a prompt to Google's Gemini model and return the response.
    """
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
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

def main():
    """Run all evaluation tasks on all models."""

    # Show help if requested
    if len(sys.argv) > 1 and sys.argv[1] in ["--help", "-h"]:
        print(__doc__)
        sys.exit(0)

    # Check API keys before doing anything
    check_api_keys()

    # Set up the API clients
    setup_clients()

    # Load the tasks
    tasks = load_tasks()
    print(f"Loaded {len(tasks)} tasks from tasks.json")

    # Define which models to run
    # Each entry is: (folder_name, api_function)
    models = [
        ("gpt-4o", call_openai),
        ("claude-sonnet", call_anthropic),
        ("gemini-pro", call_gemini),
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
                # Call the model
                response = call_model(prompt)

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
