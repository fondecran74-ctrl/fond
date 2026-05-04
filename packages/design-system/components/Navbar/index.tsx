import React from "react";

export interface NavbarProps {
  children?: React.ReactNode;
  className?: string;
}

export function Navbar({ children, className = "" }: NavbarProps) {
  return <div className={className}>{children}</div>;
}
