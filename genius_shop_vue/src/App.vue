<template>
  <div id="wrapper">
    <nav class="navbar">
      <router-link to="/" class="navbar-item">Home</router-link> | 
      <router-link to="/cart" class="navbar-item">Cart</router-link> | 
      <router-link to="/profil" class="navbar-item">Profil</router-link>
    </nav> 
  </div>
  <router-view/>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
