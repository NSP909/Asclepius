import { useState, useEffect } from "react";
import axios from "axios";
import Header from "./components/Header";
import SearchBarResults from "./components/SearchBarResults";

const SearchPredict = () => {
  return (
    <div className="flex flex-col w-full h-screen overflow-y-hidden items-center gap-10">
      <Header />
      <SearchBarResults />
    </div>
  );
};

export default SearchPredict;
