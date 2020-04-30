<template>
<v-container
  class="input-container-background"
  id="inputContainer"
  ref="inputContainer">
  <v-layout
    class="input-container">
    <div class="input">
      <v-text-field
        v-model="messageText"
        label="Message"
        outlined
        rounded
        solo
        color="primary">
      </v-text-field>
    </div>
    <div class="button-send">
      <v-btn @click="sendMessage" fab>
        <v-icon class="primary--text">mdi-send</v-icon>
      </v-btn>
    </div>
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
      this.messageText = undefined;
    }
  }
};
</script>

<style>
.input-container {
  margin-bottom: -40px;
  display: flex;
  flex-direction: row;
}

.input {
  flex: 1;
}

.button-send {
  margin-left: 15px;
}

.button-send-shadow {
  padding: 5px;
}
</style>
