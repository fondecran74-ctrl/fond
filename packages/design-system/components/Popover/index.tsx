import React from "react";

export interface PopoverProps {
  children?: React.ReactNode;
  className?: string;
}

export function Popover({ children, className = "" }: PopoverProps) {
  return <div className={className}>{children}</div>;
}
