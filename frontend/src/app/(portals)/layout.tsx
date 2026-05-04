export default function PortalLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex min-h-screen">
      <aside className="w-64 border-r bg-gray-50 p-4">
        <div className="mb-8">
          <h1 className="text-xl font-serif font-bold text-primary-900">EMS</h1>
        </div>
        <nav className="space-y-1">
          <a href="/system/dashboard" className="block rounded px-3 py-2 text-sm hover:bg-gray-100">Tableau de bord</a>
        </nav>
      </aside>
      <main className="flex-1 p-6">{children}</main>
    </div>
  );
}
