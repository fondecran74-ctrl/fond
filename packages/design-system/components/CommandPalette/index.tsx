import React from "react";

export interface CommandPaletteProps {
  children?: React.ReactNode;
  className?: string;
}

export function CommandPalette({ children, className = "" }: CommandPaletteProps) {
  return <div className={className}>{children}</div>;
}
