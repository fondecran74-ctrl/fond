export default function ProgramDetailPage({ params }: { params: { programId: string } }) {
  return (
    <div className="mx-auto max-w-7xl px-6 py-12">
      <h1 className="text-3xl font-bold">Programme {params.programId}</h1>
    </div>
  );
}
