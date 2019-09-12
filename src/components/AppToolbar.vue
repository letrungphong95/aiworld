<template>
  <div>
    <v-toolbar 
        color="deep-orange lighten-5">
        <router-link to="/foo">
            <v-toolbar-title>We are super coders!</v-toolbar-title>
        </router-link>
      <div class="flex-grow-1"></div>

      <v-toolbar-items>
        <v-btn text>About Us</v-btn>
        <v-btn text>Our Products</v-btn>
        <v-btn text>Our Contact</v-btn>
      </v-toolbar-items>
    </v-toolbar>
  </div>
</template>