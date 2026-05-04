import { test, expect } from "@playwright/test";
test("teacher portal loads", async ({ page }) => {
  await page.goto("/teacher/dashboard");
});
