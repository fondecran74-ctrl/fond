import { test, expect } from "@playwright/test";
test("admin portal loads", async ({ page }) => {
  await page.goto("/system/dashboard");
});
