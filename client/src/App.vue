<template>
  <v-app class="background-color">
    <Header></Header>
    <v-content>
      <v-container>
        <router-view></router-view>
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
};
</script>

<style>

.background-color {
  background-color: var(--v-background-base) !important;
}
</style>
