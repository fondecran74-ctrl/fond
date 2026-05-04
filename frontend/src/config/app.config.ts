export const appConfig = {
  name: "EMS",
  apiUrl: process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api/v1",
  keycloakUrl: process.env.NEXT_PUBLIC_KEYCLOAK_URL || "http://localhost:8080",
  keycloakRealm: process.env.NEXT_PUBLIC_KEYCLOAK_REALM || "ems",
  keycloakClientId: process.env.NEXT_PUBLIC_KEYCLOAK_CLIENT_ID || "ems-frontend",
};
