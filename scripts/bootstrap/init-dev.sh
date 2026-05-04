#!/bin/bash
set -euo pipefail
echo "=== Initializing development environment ==="
docker compose up -d postgres redis kafka clickhouse keycloak minio vault
cd backend && pip install -r requirements/development.txt && python manage.py migrate
cd ../frontend && pnpm install
echo "=== Development environment ready ==="
