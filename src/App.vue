<template>
  <v-app>
    <app-toolbar></app-toolbar>
    <router-view/>
    <app-footer></app-footer>
  </v-app>
</template>

<script>
import AppToolbar from './components/AppToolbar.vue';
import AppFooter from './components/AppFooter.vue';

export default {
  name: 'App',
  components: {
    AppToolbar,
    AppFooter
  },
  data: () => ({
    //
  }),
};
</script>
