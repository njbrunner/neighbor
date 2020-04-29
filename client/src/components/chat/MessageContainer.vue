<template>
  <v-container
    class="message-container"
    v-scroll
    id="test"
    ref="test">
    <Message
      v-for="(message, index) in messages"
      :key="index"
      :message="message"
      :user="user">
    </Message>

    <InputContainer
      @sendMessage="sendMessage">
    </InputContainer>
  </v-container>
</template>

<script>
import InputContainer from '@/components/chat/InputContainer';
import Message from '@/components/chat/Message';

export default {
    name: 'MessageContainer',
    props: {
      messages: Array,
      user: Object,
    },
    components: {
      InputContainer,
      Message
    },
    methods: {
      sendMessage(messageText) {
        this.channel.sendMessage(messageText)
          .then(() => {
            this.getChannelMessages();
          });
      },
    }
}
</script>

<style>
.message-container {
  margin-bottom: 100px;
  width: 100%;
}
</style>
