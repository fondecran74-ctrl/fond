import React from "react";

export interface SelectProps {
  children?: React.ReactNode;
  className?: string;
}

export function Select({ children, className = "" }: SelectProps) {
  return <div className={className}>{children}</div>;
}
