import React from "react";

export interface AvatarProps {
  children?: React.ReactNode;
  className?: string;
}

export function Avatar({ children, className = "" }: AvatarProps) {
  return <div className={className}>{children}</div>;
}
