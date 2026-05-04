import React from "react";

export interface DialogProps {
  children?: React.ReactNode;
  className?: string;
}

export function Dialog({ children, className = "" }: DialogProps) {
  return <div className={className}>{children}</div>;
}
