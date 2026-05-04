import React from "react";

export interface DropdownProps {
  children?: React.ReactNode;
  className?: string;
}

export function Dropdown({ children, className = "" }: DropdownProps) {
  return <div className={className}>{children}</div>;
}
