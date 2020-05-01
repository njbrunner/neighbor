<template>
  <div>
    <h3 class="primary--text">Login</h3>
    <v-form class="form-style">
      <v-text-field
        v-model="email"
        label="E-mail"
        prepend-inner-icon="mdi-email-outline"
        outlined
        required
      ></v-text-field>
      <v-text-field
        v-model="password"
        label="Password"
        prepend-inner-icon="mdi-lock-outline"
        outlined
        required
      ></v-text-field>
      <v-btn
        block
        color="primary"
        @click="login"
      >Login</v-btn>
    </v-form>
    <p>Not a user? <router-link class="link-login" to="/signup">Sign up.</router-link></p>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  data() {
    return {
      email: undefined,
      password: undefined
    }
  },
  methods: {
    login() {
      let loginData = {
        "email": this.email,
        "password": this.password
      }
      this.$store.dispatch('login', loginData)
      .then(() => {
        this.$router.push({'name': 'Home'});
      })
      .catch(error => {
        this.$toasted.show(error);
      });
    }
  },
}
</script>

<style>
.form-style {
  margin: 32px;
  /* margin: auto; */
}

.link-login {
  text-decoration: none;
}
</style>
