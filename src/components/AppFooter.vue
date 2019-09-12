<template>
  <v-footer
    padless
    fixed
  >
    <v-card
      class="flex"
      flat
      tile
    >
      <v-card-title class="deep-orange lighten-5">
        <strong class="subheading">Get connected with us on social networks!</strong>

        <div class="flex-grow-1"></div>

        <v-btn
          v-for="icon in icons"
          :key="icon"
          class="mx-4"
          icon
        >
          <v-icon size="24px">{{ icon }}</v-icon>
        </v-btn>
      </v-card-title>

      <v-card-actions dark class="brown lighten-4 justify-center">
        {{ new Date().getFullYear() }} — <strong>AI Course</strong>
      </v-card-actions>
    </v-card>
  </v-footer>
</template>

<script>
  export default {
    data: () => ({
      icons: [
        'fab fa-facebook',
        'fab fa-twitter',
        'fab fa-google-plus',
        'fab fa-linkedin',
        'fab fa-instagram',
      ],
    }),
  }
</script>