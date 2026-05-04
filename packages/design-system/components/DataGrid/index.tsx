import React from "react";

export interface DataGridProps {
  children?: React.ReactNode;
  className?: string;
}

export function DataGrid({ children, className = "" }: DataGridProps) {
  return <div className={className}>{children}</div>;
}
