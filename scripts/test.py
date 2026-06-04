import subprocess
import sys


def main() -> None:
    completed = subprocess.run(
        [sys.executable, "-m", "pytest", "-m", "not live", "tests"],
        check=False,
    )
    raise SystemExit(completed.returncode)


if __name__ == "__main__":
    main()
