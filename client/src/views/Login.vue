<template>
  <v-container class="vertical-horizontal-center">
    <v-row class="container-login">
      <v-col class="container-logo">
        <h3 class="text-align-center">COVID-19</h3>
      </v-col>
      <v-col class="container-form">
        <h3>Login</h3>
        <v-form class="form-style">
          <v-text-field
            v-model="name"
            :rules="nameRules"
            label="Name"
            outlined
            required
          ></v-text-field>
          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            outlined
            required
          ></v-text-field>
          <v-select
            :items="['test 1', 'test 2']"
            label="Test"
            outlined
            color="primary"
          ></v-select>
          <v-btn
            outlined
            block
            color="primary"
          >Login</v-btn>
        </v-form>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      nameRules: {

      }
    }
  }
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
</style>
