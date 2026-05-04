# Architecture Overview

## EMS — Education Management System

Architecture monolithe modulaire Django avec séparation IAM/Backend/Frontend.

### Composants principaux
- **Backend** : Django 5.2 LTS — monolithe modulaire
- **Frontend** : Next.js 15.5 — App Router
- **IAM** : Keycloak 26.5
- **Base de données** : PostgreSQL 16 avec RLS
- **Cache** : Redis 7.2
- **Event Streaming** : Apache Kafka 3.9
- **Analytics** : ClickHouse 24.3
- **Policy Engine** : OPA + Casbin
- **Gateway** : Kong 3.9
