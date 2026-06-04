import subprocess
import sys


PATHS = ("anipics", "tests", "examples")


def run(command: list[str]) -> None:
    completed = subprocess.run(command, check=False)
    if completed.returncode:
        raise SystemExit(completed.returncode)


def main() -> None:
    run([sys.executable, "-m", "black", "--target-version", "py310", *PATHS])
    run([sys.executable, "-m", "isort", "--profile", "black", *PATHS])
    run([sys.executable, "-m", "ruff", "check", "--fix", *PATHS])


if __name__ == "__main__":
    main()
