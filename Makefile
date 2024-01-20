format:
	poetry run black anipics/ tests/ setup.py
	poetry run isort --profile black anipics/ tests/ setup.py
	poetry run ruff --fix anipics/ tests/ setup.py

tests:
	poetry run pytest tests/

.PHONY: format tests