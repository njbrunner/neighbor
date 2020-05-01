<template>
<div>
  <FormContainer>
    <component :is="loginForm"></component>
  </FormContainer>
</div>
</template>

<script>
import FormContainer from '@/components/landingPage/FormContainer';
import LoginForm from '@/components/landingPage/LoginForm';
import axios from 'axios';

export default {
  name: "Login",
  components: {
    FormContainer,
    LoginForm
  },
  data() {
    return {
      loginForm: 'LoginForm',
    }
  }
};
</script>

<style>
</style>
