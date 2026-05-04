"use client";
import { createContext, useContext } from "react";

const PortalContext = createContext({});

export function PortalProvider({ children }: { children: React.ReactNode }) {
  return <PortalContext.Provider value={{}}>{children}</PortalContext.Provider>;
}

export function usePortal() {
  return useContext(PortalContext);
}
