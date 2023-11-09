<template>
  <div id="app">
    <header>
      <h1>Welcome to the Restaurant Review Analyzer</h1>
    </header>
    <main>
      <ReviewForm />
    </main>
    <footer>
      <p>© 2023 Review Analyzer</p>
    </footer>
  </div>
</template>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

header {
  padding: 20px;
  background-color: #34495e;
  color: #fff;
}

footer {
  padding: 20px;
  background-color: #2c3e50;
  color: #fff;
  position: absolute;
  bottom: 0;
  width: 95vw;
}

/* Add some more styling as per your aesthetic preference */
</style>
