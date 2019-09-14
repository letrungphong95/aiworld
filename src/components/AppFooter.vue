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
        <strong class="subheading">Get connected with me on social networks!</strong>

        <div class="flex-grow-1"></div>

        <v-btn
          v-for="icon in icons"
          :key="icon[0]"
          class="mx-4"
          :href="icon[1]"
          target="_blank"
        >
          <v-icon size="24px">{{ icon[0] }}</v-icon>
        </v-btn>
      </v-card-title>

      <v-card-actions dark class="grey lighten-1 justify-center">
        {{ new Date().getFullYear() }} — <strong>AI World</strong>
      </v-card-actions>
    </v-card>
  </v-footer>
</template>

<script>
  export default {
    data: () => ({
      icons: [
        ['fab fa-facebook','https://www.facebook.com/phong.le.39982'],
        ['fab fa-twitter','https://twitter.com/PhongLe_1995'],
        ['fab fa-linkedin', 'https://www.linkedin.com/in/le-phong-b28599178/']
      ],
    }),
  }
</script>