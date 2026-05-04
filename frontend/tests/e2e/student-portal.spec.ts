import { test, expect } from "@playwright/test";
test("student portal loads", async ({ page }) => {
  await page.goto("/student/dashboard");
});
