export default function ResearchProjectPage({ params }: { params: { projectId: string } }) {
  return (
    <div className="mx-auto max-w-7xl px-6 py-12">
      <h1 className="text-3xl font-bold">Projet de recherche {params.projectId}</h1>
    </div>
  );
}
