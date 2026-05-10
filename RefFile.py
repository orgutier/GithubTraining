"""
Reference Python file for Git training repository.

Purpose:
- Demonstrate Git tracking on source files
- Provide simple examples for commits, diffs, and merges
- Safe to modify during training exercises
"""

from datetime import datetime


APP_NAME = "git-training-repo"
VERSION = "1.0.0"


def greet_user(name: str) -> str:
    """
    Return a greeting message.
    """
    return f"Welcome to {APP_NAME}, {name}!"


def calculate_sum(a: int, b: int) -> int:
    """
    Simple function used for diff examples.
    """
    return a + b


def get_timestamp() -> str:
    """
    Return current timestamp in ISO format.
    """
    return datetime.now().isoformat()


def main() -> None:
    """
    Entry point for demonstration execution.
    """
    print("=" * 40)
    print(greet_user("Developer"))
    print(f"Version: {VERSION}")
    print(f"Timestamp: {get_timestamp()}")
    print(f"2 + 3 = {calculate_sum(2, 3)}")
    print("=" * 40)


if __name__ == "__main__":
    main()