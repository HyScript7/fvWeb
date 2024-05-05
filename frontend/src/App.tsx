import type { Component } from "solid-js";
import { Route } from "@solidjs/router";
import Home from "./pages/Home";

const App: Component = () => {
  return (
    <>
      <Route path="/" component={Home} />
    </>
  );
};

export default App;
