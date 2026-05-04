"use client";
import { createContext, useContext } from "react";

const I18nContext = createContext({});

export function I18nProvider({ children }: { children: React.ReactNode }) {
  return <I18nContext.Provider value={{}}>{children}</I18nContext.Provider>;
}

export function useI18n() {
  return useContext(I18nContext);
}
