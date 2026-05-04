import React from "react";

export interface ProgressProps {
  children?: React.ReactNode;
  className?: string;
}

export function Progress({ children, className = "" }: ProgressProps) {
  return <div className={className}>{children}</div>;
}
