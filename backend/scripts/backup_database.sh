#!/bin/bash
set -euo pipefail
pg_dump -h ${DB_HOST:-localhost} -U ${DB_USER:-ems_user} -d ${DB_NAME:-ems} -F c -f backup_$(date +%Y%m%d_%H%M%S).dump
echo "Backup completed."
