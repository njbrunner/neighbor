<template>
  <v-container class="vertical-horizontal-center">
    <v-row class="container-login">
      <v-col class="container-logo">
        <h3 class="text-align-center">COVID-19</h3>
      </v-col>
      <v-col class="container-form">
        <h3>Sign Up</h3>
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
            prepend-inner-icon="mdi-account-outline"
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
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
export default {
  name: "Signup",
  data() {
    return {
      email: undefined,
      password: undefined,
      confirmPassword: undefined,
      role: undefined
    }
  },
  methods: {
    signupUser() {
      let userData = {
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
  computed: {
    roles() {
      return this.$store.getters.getRoles;
    }
  },
  created() {
      this.$store.dispatch('getRoles');
  },
};
</script>

<style>
.vertical-horizontal-center {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.container-login {
  width: 100%;
  border: solid 2px var(--v-primary-base)
}

.container-logo {
  height: auto;
  width: 100%;
  display: flex;
  background-color: var(--v-primary-base)
}

.container-form {
  height: auto;
  width: 100%;
}

.text-align-center {
  text-align: center;
  margin: auto;
}

.form-style {
  margin: 32px;
  /* margin: auto; */
}

.link-signup {
  text-decoration: none;
}
</style>
