# src/study_chatbot/__init__.py
import os, sys, subprocess
from pathlib import Path


def main():
    # Resolve path to app.py inside the package
    entry = Path(__file__).parent / "app.py"
    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "chainlit",
            "run",
            str(entry),
            "--host",
            "0.0.0.0",
            "--port",
            os.getenv("PORT", "8000"),
        ]
    )
