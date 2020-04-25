<template>
<v-container
  class="input-container-background"
  id="inputContainer"
  ref="inputContainer">
  <v-layout
    class="input-container">
    <v-flex xs11>
      <v-text-field
        v-model="messageText"
        label="Message"
        outlined
        rounded
        solo
        color="primary">
      </v-text-field>
    </v-flex>
    <v-flex xs1 class="text-align-center">
      <v-btn @click="sendMessage" fab>
        <v-icon class="primary--text">mdi-send</v-icon>
      </v-btn>
    </v-flex>
  </v-layout>
</v-container>
</template>

<script>
export default {
  name: 'InputContainer',
  data() {
    return {
      messageText: undefined
    }
  },
  methods: {
    sendMessage() {
      this.$emit('sendMessage', this.messageText);
    }
  }
};
</script>

<style>
.input-container-background {
  padding-top: 16px;
  position: fixed;
  bottom: 0;
  width: 100%;
  min-width: inherit;
  background-color: white;
}
.input-container {
  width: inherit;
  max-width: inherit;
}

.button-send-shadow {
  padding: 5px;
}

.text-align-center {
  text-align: center;
  margin: 0;
}
</style>
