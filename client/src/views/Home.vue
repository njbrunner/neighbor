<template>
  <div class="home">
    <h1>Home Page</h1>
    <!-- <form action="https://auth.did.app/oidc/authorize" method="get">
      <input name="client_id" value="test_Q5KWXO7n" type="hidden" />
      <input name="redirect_uri" value="https://covid-19-hackathon-app.herokuapp.com/authorize/" type="hidden" />
      <input name="response_mode" value="form_post" type="hidden" />

      <button type="submit">Sign in</button>
    </form> -->
    <mode-selection :role=roleDefined></mode-selection>
  </div>
</template>

<script>
import ModeSelection from '@/components/ModeSelection';

export default {
  name: 'Home',
  data() {
    return {
      roleDefined: true
    }
  },
  components: {
    ModeSelection
  }
}
</script>
