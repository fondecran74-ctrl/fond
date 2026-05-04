"use client";

export default function Error({ error, reset }: { error: Error; reset: () => void }) {
  return (
    <div className="flex min-h-screen items-center justify-center">
      <div className="text-center">
        <h2 className="text-2xl font-bold">Une erreur est survenue</h2>
        <p className="mt-2 text-gray-600">{error.message}</p>
        <button onClick={reset} className="mt-4 rounded bg-primary-600 px-4 py-2 text-white">
          Réessayer
        </button>
      </div>
    </div>
  );
}
