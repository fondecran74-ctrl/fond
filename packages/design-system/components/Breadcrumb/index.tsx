import React from "react";

export interface BreadcrumbProps {
  children?: React.ReactNode;
  className?: string;
}

export function Breadcrumb({ children, className = "" }: BreadcrumbProps) {
  return <div className={className}>{children}</div>;
}
