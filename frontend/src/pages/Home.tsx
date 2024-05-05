import { Component } from "solid-js";
import { A } from '@solidjs/router'

const Home: Component = () => {
  return (
    <div>
      <p class="text-2xl text-purple-500">fvWeb</p>
      <p><A href="/about" class="link text-purple-600 hover:text-purple-700">About</A></p>
    </div>
  );
};

export default Home;
