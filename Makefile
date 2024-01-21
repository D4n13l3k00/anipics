format:
	poetry run black anipics/ tests/ examples/
	poetry run isort --profile black anipics/ tests/ examples/
	poetry run ruff --fix anipics/ tests/ examples/

tests:
	poetry run pytest tests/

.PHONY: format tests