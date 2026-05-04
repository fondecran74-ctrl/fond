import React from "react";

export interface CheckboxProps {
  children?: React.ReactNode;
  className?: string;
}

export function Checkbox({ children, className = "" }: CheckboxProps) {
  return <div className={className}>{children}</div>;
}
