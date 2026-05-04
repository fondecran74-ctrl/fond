export default function PublicLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-white">
      <header className="border-b bg-white px-6 py-4">
        <nav className="mx-auto flex max-w-7xl items-center justify-between">
          <a href="/" className="text-2xl font-serif font-bold text-primary-900">EMS</a>
          <div className="flex gap-6">
            <a href="/site/about" className="text-gray-600 hover:text-primary-600">À propos</a>
            <a href="/programs" className="text-gray-600 hover:text-primary-600">Programmes</a>
            <a href="/research" className="text-gray-600 hover:text-primary-600">Recherche</a>
            <a href="/login" className="rounded bg-primary-600 px-4 py-2 text-white hover:bg-primary-700">Connexion</a>
          </div>
        </nav>
      </header>
      <main>{children}</main>
    </div>
  );
}
