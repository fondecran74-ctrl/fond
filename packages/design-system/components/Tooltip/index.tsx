import React from "react";

export interface TooltipProps {
  children?: React.ReactNode;
  className?: string;
}

export function Tooltip({ children, className = "" }: TooltipProps) {
  return <div className={className}>{children}</div>;
}
