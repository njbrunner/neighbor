<template>
  <v-app-bar app light id="appBar" ref="appBar">
    <img
      class="mr-3 pointer"
      :src="require('@/assets/images/neighbor_150x50.png')"
      height="50"
      @click="goHome"/>

    <v-spacer></v-spacer>

      <v-btn
        icon
        @click="goToChat">
        <v-icon class="primary--text">mdi-chat-outline</v-icon>
      </v-btn>

      <v-menu open-on-hover offset-y v-if="isLoggedIn">
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon class="primary--text">mdi-account-outline</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item @click="logout">
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
  </v-app-bar>
</template>

<script>
export default {
  name: "Header",
  props: {
    user: Object
  },
  methods: {
    logout() {
      this.$store.dispatch('logout');
      this.$router.push({'name': 'Login'});
    },
    goHome() {
      this.$router.push({name: 'Home'});
    },
    goToChat() {
      this.$router.push({name: 'Chat', params: {user: this.user}});
    }
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    }
  },
};
</script>

<style>
.pointer {
  cursor: pointer;
}
</style>
