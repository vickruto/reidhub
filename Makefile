# Self-documenting Makefile for Fynesse Template

.DEFAULT_GOAL := help

.PHONY: install dev test coverage format lint type-check quality check clean help

install: ## 📦 Install Python dependencies
	poetry install

dev: ## 📦 Install Python dependencies (with dev tools)
	poetry install --with dev

test: ## 🧪 Run tests
	poetry run pytest

coverage: ## 🧪 Run tests with coverage
	poetry run pytest --cov=reidhub

format: ## 🎨 Format code with black
	poetry run black reidhub/

lint: ## 🔍 Run flake8 linting
	poetry run flake8 reidhub/

type-check: ## 🔎 Run mypy type checking
	poetry run mypy reidhub/

yamllint: ## 🧑‍💻 Lint YAML files using yamllint
	poetry run yamllint . --config-file .yamllint

quality: format lint type-check ## ✅ Run code quality checks (format + lint + type-check)

check: test format lint type-check ## 🚦 Run full validation (tests + format + lint + type-check)

clean: ## 🧹 Clean cache and build artifacts
	rm -rf .pytest_cache .mypy_cache .coverage dist build
	find . -type d -name "__pycache__" -exec rm -rf {} +

render-docs: ## 📝 Render documentation files from templates using render.py
	cd docs && poetry run python render.py

build-docs: render-docs ## 📝 Build MkDocs documentation after rendering
	mkdocs build

serve-docs: render-docs ## 🌐 Serve MkDocs documentation locally after rendering
	mkdocs serve

deploy-docs: render-docs ## 🚀 Deploy MkDocs documentation (force option) after rendering
	mkdocs gh-deploy --force

help: ## 📖 Show available commands
	@echo "Available rules:"
	@grep -E '^[a-zA-Z_-]+:.*?##' $(MAKEFILE_LIST) \
		| sed -E 's/:.*##/|/' \
		| column -t -s '|'
