# EMS — Education Management System

Plateforme de gestion universitaire enterprise, multi-établissement, multi-campus.

## Architecture

- **Backend** : Django 5.2 LTS + DRF 3.16 + Channels 4.3
- **Frontend** : Next.js 15.5 + React 19.2 + TypeScript 5.8
- **IAM** : Keycloak 26.5 (OIDC/SAML)
- **Database** : PostgreSQL 16 avec RLS
- **Cache/Broker** : Redis 7.2
- **Event Streaming** : Apache Kafka 3.9
- **Analytics** : ClickHouse 24.3
- **Storage** : MinIO (S3-compatible)
- **Policy Engine** : OPA 1.12 + Casbin
- **Secrets** : HashiCorp Vault 1.20
- **Gateway** : Kong 3.9
- **Orchestration** : Kubernetes 1.34 + Helm 3.19
- **Observability** : Prometheus 3.0 + Grafana 11.6

## Principe fondamental

**Aucun auto-enregistrement.** Toute identité est créée exclusivement par un agent habilité de l'établissement.

## Démarrage rapide

```bash
# Backend
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements/development.txt
python manage.py migrate
python manage.py runserver

# Frontend
cd frontend
pnpm install
pnpm dev
```

## Structure

```
platform/
├── backend/          # Django monolithe modulaire
├── frontend/         # Next.js 15 App Router
├── packages/         # Shared packages (contracts, design-system, shared-kernel)
├── infrastructure/   # Helm, K8s, monitoring, security
├── docs/             # Architecture, ADR, runbooks, compliance
└── scripts/          # Bootstrap, CI, release, migrations
```
