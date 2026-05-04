import React from "react";

export interface SwitchProps {
  children?: React.ReactNode;
  className?: string;
}

export function Switch({ children, className = "" }: SwitchProps) {
  return <div className={className}>{children}</div>;
}
