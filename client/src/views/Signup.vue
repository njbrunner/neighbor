<template>
<div>
  <FormContainer>
    <component :is="signupForm"></component>
  </FormContainer>
</div>
</template>

<script>
import FormContainer from '@/components/landingPage/FormContainer';
import SignupForm from '@/components/landingPage/SignupForm';

export default {
  name: "Signup",
  components: {
    FormContainer,
    SignupForm
  },
  data() {
    return {
      signupForm: 'SignupForm'
    }
  }
};
</script>

<style>
</style>
