<template>
  <v-container class="vertical-horizontal-center">
    <v-row class="container-login">
      <v-col class="container-logo">
        <img
          src="@/assets/images/neighbor_150x50.png"
          height="50"
          width="150"
          aspect-ratio="3"
          class="logo"/>
      </v-col>
      <v-col class="container-form">
        <slot></slot>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'FormContainer',

}
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
  border-radius: 10px;
  border: solid 1px lightgrey;
  box-shadow: 2px 4px 5px rgba(0, 0, 0, .19);

}

.container-logo {
  text-align: center;
  border-right: solid 2px var(--v-primary-base);
  margin-top: 32px;
  margin-bottom: 32px;
  position: relative;
}

.logo {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.container-form {
  height: auto;
  width: 100%;
  text-align: center;
  padding-top: 32px;
}

.text-align-center {
  text-align: center;
  margin: auto;
}
</style>
