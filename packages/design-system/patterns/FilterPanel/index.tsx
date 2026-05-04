import React from "react";

export function FilterPanel({ children, className = "" }: { children?: React.ReactNode; className?: string }) {
  return <div className={className}>{children}</div>;
}
