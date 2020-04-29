<template>
<div>
  <h1 v-if="channel">{{ channel.friendlyName }}</h1>
  <hr>

  <v-row>
    <v-col
      :cols="3">
      <ChatSidebar></ChatSidebar>
    </v-col>
    <v-col
      :cols="9">
      <MessageContainer
        :messages="channelMessages"
        :user="user">
      </MessageContainer>
    </v-col>
  </v-row>



</div>
</template>

<script>
const Chat = require('twilio-chat');
import ChatSidebar from '@/components/chat/ChatSidebar';
import MessageContainer from '@/components/chat/MessageContainer';

export default {
    name: 'Chat',
    props: {
        user: Object
    },
    components: {
      ChatSidebar,
      MessageContainer
    },
    data() {
      return {
        chatClient: undefined,
        channel: undefined,
        channelUniqueName: 'test',
        channelFriendlyName: 'Test Channel',
        channelMessages: undefined,
        channels: undefined
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
          });
      },
      getChannelMessages() {
        this.channel.getMessages()
          .then(messages => {
            this.channelMessages = messages.items;
            this.subscribeToNewMessages();
          });
      },
      subscribeToNewMessages() {
        this.channel.on('messageAdded', (message) => {
          this.channelMessages.push(message);
        });
      },
      sendMessage(messageText) {
        this.channel.sendMessage(messageText)
          .then(() => {
            this.getChannelMessages();
          });
      },
      createChatClient() {
        Chat.Client.create(this.user.auth_token, {'username': 'test'})
        .then((client) => {
          this.chatClient = client;
          this.subscribeToExpiredToken();
          this.doesChannelExist(this.channelUniqueName);
        })
        .catch(error => {
          console.log(error.message);
          if (error.message.toLowerCase().includes('access token expired')) {
            console.log('YUP!');
            //TODO: call refresh token route
          }
        });
      },
      subscribeToExpiredToken() {
        this.chatClient.on('tokenExpired', () => {

        })
      }
    },
    created() {
      this.createChatClient();
    }
}
</script>

<style>
</style>
