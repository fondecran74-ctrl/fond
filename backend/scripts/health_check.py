"""Health check script."""
import requests
import sys

try:
    r = requests.get("http://localhost:8000/health/", timeout=5)
    if r.status_code == 200:
        print("Health check passed")
        sys.exit(0)
    print(f"Health check failed: {r.status_code}")
    sys.exit(1)
except Exception as e:
    print(f"Health check error: {e}")
    sys.exit(1)
