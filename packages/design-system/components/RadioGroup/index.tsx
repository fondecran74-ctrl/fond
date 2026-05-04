import React from "react";

export interface RadioGroupProps {
  children?: React.ReactNode;
  className?: string;
}

export function RadioGroup({ children, className = "" }: RadioGroupProps) {
  return <div className={className}>{children}</div>;
}
