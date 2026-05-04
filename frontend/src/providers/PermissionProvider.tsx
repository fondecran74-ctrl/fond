"use client";
import { createContext, useContext } from "react";

const PermissionContext = createContext({});

export function PermissionProvider({ children }: { children: React.ReactNode }) {
  return <PermissionContext.Provider value={{}}>{children}</PermissionContext.Provider>;
}

export function usePermission() {
  return useContext(PermissionContext);
}
