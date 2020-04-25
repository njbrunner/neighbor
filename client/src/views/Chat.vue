<template>
<div>
  <h1 v-if="channel">{{ channel.friendlyName }}</h1>
  <hr>

  <MessageContainer
    :messages="channelMessages"
    :user="user">
  </MessageContainer>

  <InputContainer
    @sendMessage="sendMessage">
  </InputContainer>

</div>
</template>

<script>
const Chat = require('twilio-chat');
import MessageContainer from '@/components/chat/MessageContainer';
import InputContainer from '@/components/chat/InputContainer';

export default {
    name: 'Chat',
    props: {
        user: Object
    },
    components: {
      MessageContainer,
      InputContainer
    },
    data() {
      return {
        chatClient: undefined,
        channel: undefined,
        channelUniqueName: 'test',
        channelFriendlyName: 'Test Channel',
        channelMessages: undefined
      }
    },
    methods: {
      doesChannelExist(uniqueName) {
        this.chatClient.getChannelByUniqueName(uniqueName)
          .then(channel => {
            console.log(this.channelFriendlyName + ' exists');
            this.channel = channel;
            this.isUserAChannelMemeber();
          })
          .catch(() => {
            console.log('Channel does not yet exist');
            this.createChannel();
          })
      },
      isUserAChannelMemeber() {
        this.chatClient.getSubscribedChannels()
          .then(channels => {
            if (channels.items != 0) {
              if (this.channel.uniqueName == channels.items[0].state.uniqueName) {
                console.log('Already a member of ' + this.channelFriendlyName);
                this.getChannelMessages()
              } else {
                console.log('Not yet a member of ' + this.channelFriendlyName);
                this.joinChannel(this.channel);
              }
            } else {
              this.joinChannel(this.channel);
            }
          });
      },
      joinChannel() {
        this.channel.join()
          .then((channel) => {
            console.log('Joined channel: ' + channel.friendlyName);
            this.getChannelMessages();
          });
      },
      createChannel() {
        this.chatClient.createChannel({
          uniqueName: this.channelUniqueName,
          friendlyName: this.channelFriendlyName
        })
          .then(channel => {
            console.log('Created new channel: ' + channel.friendlyName);
            this.channel = channel;
            this.joinChannel();
          })
      },
      getChannelMessages() {
        this.channel.getMessages()
          .then(messages => {
            this.channelMessages = messages.items;
          })
      },
      sendMessage(messageText) {
        this.channel.sendMessage(messageText)
          .then(() => {
            this.getChannelMessages();
          });
      }
    },
    created() {
      Chat.Client.create(this.user.auth_token, {'username': 'test'})
        .then((client) => {
          this.chatClient = client;
          this.doesChannelExist(this.channelUniqueName);
        });
    },
    updated(){
      // console.log(this.$refs.inputContainer);
      // console.log(this.$refs.inputContainer.offsetHeight);
      // console.log(document.documentElement.clientHeight);
      // console.log(window.innerHeight);
      // console.log(document.getElementById('#appBar'));
      if (this.channelMessages) {
        let container = this.$refs.test;
        container.scrollTop = container.scrollHeight;
        document.body.scrollTop = container.scrollHeight;
      }
    },
}
</script>

<style>
</style>
