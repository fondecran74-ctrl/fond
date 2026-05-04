import React from "react";

export interface TableProps {
  children?: React.ReactNode;
  className?: string;
}

export function Table({ children, className = "" }: TableProps) {
  return <div className={className}>{children}</div>;
}
