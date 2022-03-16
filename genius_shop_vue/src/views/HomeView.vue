<template>
  <div class="home">
    <section class="hero is-medium is-dark">
        <div class="hero-body has-text-centered">
            <p class="title">
                Genius Shop
            </p>
        </div>
    </section>

    <div class="columns is-multiline">
      <div 
        class="colms is-3"
        v-for="product in latestProducts"
        v-bind:key="product.id"
        >
        <div class="box">
          <h3 class="is-size-4">{{ product.name }}</h3>
          <h3 class="is-size-12">{{ product.price }} €</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      latestProducts: []
    }
  },
  components: {
  },
  mounted() {
    this.getLatestProducts()
  },
  methods: {
    getLatestProducts() {
      axios
        .get("http://127.0.0.1:8000/products/")
        .then(response => {
          this.latestProducts = response.data
        })
    }
  }
}
</script>

 