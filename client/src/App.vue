<template>
  <v-app class="background-color">
    <Header :user="user"></Header>
    <v-content>
      <v-container>
        <router-view :user="user"></router-view>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Header from '@/components/Header';

export default {
  name: 'App',
  components: {
    Header
  },
  computed: {
    user() {
      return this.$store.getters.getUser;
    }
  },
};
</script>

<style>

.background-color {
  background-color: var(--v-background-base) !important;
}
</style>
