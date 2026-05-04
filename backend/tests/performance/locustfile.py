"""Locust load test file."""
from locust import HttpUser, task, between


class EMSUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def list_courses(self):
        self.client.get("/api/v1/catalog/courses/")

    @task(1)
    def health_check(self):
        self.client.get("/health/")
