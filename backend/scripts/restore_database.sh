#!/bin/bash
set -euo pipefail
if [ -z "$1" ]; then echo "Usage: $0 <backup_file>"; exit 1; fi
pg_restore -h ${DB_HOST:-localhost} -U ${DB_USER:-ems_user} -d ${DB_NAME:-ems} -c "$1"
echo "Restore completed."
