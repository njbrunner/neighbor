<template>
<div>
  <h3 class="primary--text">Sign Up</h3>
  <v-form class="form-style">
    <v-text-field
      v-model="name"
      label="Name"
      prepend-inner-icon="mdi-account-outline"
      outlined
      required>
    </v-text-field>
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
    <v-text-field
      v-model="confirmPassword"
      label="Confirm Password"
      prepend-inner-icon="mdi-lock-outline"
      outlined
      required
    ></v-text-field>
    <v-select
      v-model="role"
      :items="roles"
      label="How would you like to participate?"
      prepend-inner-icon="mdi-form-select"
      outlined
      color="primary"
      item-text="label"
      item-value="id"
    ></v-select>
    <v-btn
      block
      color="primary"
      @click="signupUser"
    >Sign Up</v-btn>
  </v-form>
  <p>Already a user? <router-link class="link-signup" to="/login">Login.</router-link></p>
</div>
</template>

<script>
export default {
  name: 'SignupForm',
  data() {
    return {
      name: undefined,
      email: undefined,
      password: undefined,
      confirmPassword: undefined,
      role: undefined
    }
  },
  computed: {
    roles() {
      return this.$store.getters.getRoles;
    }
  },
  methods: {
    signupUser() {
      let userData = {
        "name": this.name,
        "email": this.email,
        "password": this.password,
        "role": {
          "id": this.role
        }
      }
      this.$store.dispatch('signup', userData)
      .then(() => {
        this.$router.push({'name': 'Home'});
      })
      .catch(error => {
        this.$toasted.show(error);
        console.log(error);
      });
    }
  },
  created() {
      this.$store.dispatch('getRoles');
  },
}
</script>

<style>
.form-style {
  margin: 32px;
  /* margin: auto; */
}

.link-signup {
  text-decoration: none;
}
</style>
