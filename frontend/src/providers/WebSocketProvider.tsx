"use client";
import { createContext, useContext } from "react";

const WebSocketContext = createContext({});

export function WebSocketProvider({ children }: { children: React.ReactNode }) {
  return <WebSocketContext.Provider value={{}}>{children}</WebSocketContext.Provider>;
}

export function useWebSocket() {
  return useContext(WebSocketContext);
}
