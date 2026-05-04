import type { Metadata } from "next";
import "@/styles/globals.css";
import { Providers } from "@/providers/QueryProvider";

export const metadata: Metadata = {
  title: "EMS — Education Management System",
  description: "Plateforme de gestion universitaire enterprise",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr">
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
