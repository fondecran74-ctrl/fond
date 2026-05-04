#!/bin/bash
set -euo pipefail

echo "=== EMS Backend Bootstrap ==="
python -m venv .venv
source .venv/bin/activate
pip install -r requirements/development.txt
python manage.py migrate
python manage.py collectstatic --noinput
echo "=== Bootstrap complete ==="
