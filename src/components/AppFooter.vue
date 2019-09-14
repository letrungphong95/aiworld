<template>
  <v-footer
    padless
    absolute
  >
    <v-card
      class="flex"
      flat
      tile
    >
      <v-card-title class="grey lighten-5">
        <strong class="subheading">Get connected and chill with me on social networks!</strong>

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

      <v-card-actions dark class="grey lighten-1 justify-center">
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