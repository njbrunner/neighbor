<template>
  <v-container
    class="message-container"
    v-if="selectedChannel">
    <h1>{{ selectedChannel.friendlyName }}</h1>
    <hr>
    <div class="messages" ref="messageBody">
      <Message
        v-for="(message, index) in messages"
        :key="index"
        :message="message"
        :user="user">
      </Message>
    </div>

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
    components: {
      InputContainer,
      Message
    },
    props: {
      selectedChannel: Object,
      user: Object,
    },
    data() {
      return {
        messages: undefined
      }
    },
    methods: {
      sendMessage(messageText) {
        this.selectedChannel.sendMessage(messageText)
          .then(() => {
            this.getChannelMessages();
          });
      },
      getChannelMessages() {
        console.log('get channel messages');
        this.selectedChannel.getMessages()
          .then(messages => {
            this.messages = messages.items;
            // this.subscribeToNewMessages();
          });
      },
      subscribeToNewMessages() {
        this.selectedChannel.on('messageAdded', (message) => {
          this.messages.push(message);
        });
      },
      scrollToBottom() {
        console.log('scroll to bottom');
        const messageBody = this.$refs.messageBody;
        messageBody.scrollTop = 10000000000;
      }
    },
    updated() {
      this.getChannelMessages()
    }
}
</script>

<style>
.message-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  height: calc(100vh - 65px);
}

.messages {
  display: flex;
  flex-direction: column;
  flex: 1;
  overflow-y: scroll;
}
</style>
