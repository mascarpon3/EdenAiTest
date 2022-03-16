<template>
  <div class="home">
    <section class="hero is-medium is-dark">
        <div class="hero-body has-text-centered">
            <p class="title">
                Genius Shop
            </p>
        </div>
    </section>

    <div class="box">
      <button v-on:click="sortByName()">sort by name</button>
      <button v-on:click="sortByPrice()">sort by price</button>
    </div>

    <div class="columns is-multiline">
      <div 
        class="col-3"
        v-for="product in filteredProducts"
        v-bind:key="product.id"
        >
        <div class="box">
          <h3 class="is-size-4">{{ product.name }}</h3>
          <h4 class="is-size-12">{{ product.price }} €</h4>
          <h4 class="is-size-12">{{ product.department }} </h4>
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
      allProducts: [],
      filteredProducts: [],
      sortDescending: true,
      minPrice: 0,
      maxPrice: Infinity,
    }
  },
  components: {
  },
  mounted() {
    this.getAllProducts()
  },
  methods: {
    getAllProducts() {
      axios
        .get("http://127.0.0.1:8000/products/")
        .then(response => {
          this.allProducts = response.data
          this.filteredProducts = response.data
      })
    },
    sortByName(){
      if(this.sortDescending){
        this.filteredProducts = this.filteredProducts.sort(compareNames)
      }
      else{
        this.filteredProducts = this.filteredProducts.sort(compareNames).reverse();
      }
      this.sortDescending = !this.sortDescending    
    },
    sortByPrice(){
      if(this.sortDescending){
        this.filteredProducts = this.filteredProducts.sort(comparePrices)
      }
      else{
        this.filteredProducts = this.filteredProducts.sort(comparePrices).reverse();
      }
      this.sortDescending = !this.sortDescending    
    },
  }
}

function sortBy(allProducts, compareMethod, sortDescending){  
  if(sortDescending){
    return allProducts.sort(compareMethod).reverse()
  }else{
    return allProducts.sort(compareMethod)
  }
}

function compareNames(product1, product2) {
  if (product1.name < product2.name)
     return 1;
  if (product1.name > product2.name)
    return -1;
  return 0;
}

function comparePrices(product1, product2) {
  if (product1.price < product2.price)
     return 1;
  if (product1.price > product2.price)
    return -1;
  return 0;
}
</script>

 