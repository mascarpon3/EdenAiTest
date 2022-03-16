<template>
  <div id="wrapper">
    <nav class="navbar">
      <router-link to="/" class="button">Home</router-link>
      <router-link to="/cart" class="button">Cart</router-link>
      <router-link to="/profil" class="button">Profil</router-link>
    </nav> 
  </div>
  <router-view/>
</template>


<style lang="scss">
@import "https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css"
</style>