SHELL := /bin/bash
.DEFAULT_GOAL := help

.PHONY: help dev build test lint clean

help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

dev: ## Start development environment
	docker compose up -d postgres redis kafka clickhouse keycloak minio vault

dev-all: ## Start all services including backend and frontend
	docker compose up -d

build: ## Build all Docker images
	docker compose build

test-backend: ## Run backend tests
	cd backend && python -m pytest

test-frontend: ## Run frontend tests
	cd frontend && pnpm test

lint-backend: ## Lint backend
	cd backend && ruff check . && mypy .

lint-frontend: ## Lint frontend
	cd frontend && pnpm lint

clean: ## Clean generated files
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name node_modules -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .next -exec rm -rf {} + 2>/dev/null || true
