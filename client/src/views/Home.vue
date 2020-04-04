<template>
  <div class="home">
    <h1>COVID-19 HACKATHON APP</h1>
    <form action="https://auth.did.app/oidc/authorize" method="get">
      <input name="client_id" value="test_Q5KWXO7n" type="hidden" />
      <input name="redirect_uri" value="https://njbrunner.github.io/covid-19/" type="hidden" />
      <input name="response_mode" value="form_post" type="hidden" />

      <button type="submit">Sign in</button>
    </form>
  </div>
</template>

<script>

export default {
  name: 'Home',
}
</script>
