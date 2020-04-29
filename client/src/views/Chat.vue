<template>
<div>
  <v-row>
    <v-col
      :cols="3">
      <ChatSidebar
        :channels="channels"
        @onSelectedChannel="onSelectedChannel">
      </ChatSidebar>
    </v-col>
    <v-col
      :cols="9">
      <MessageContainer
        :user="user"
        :selectedChannel="selectedChannel">
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
        // channelUniqueName: 'test',
        // channelFriendlyName: 'Test Channel',
        channels: undefined,
        selectedChannel: undefined
      }
    },
    methods: {
      // doesChannelExist(uniqueName) {
      //   this.chatClient.getChannelByUniqueName(uniqueName)
      //     .then(channel => {
      //       console.log(this.channelFriendlyName + ' exists');
      //       this.channel = channel;
      //       this.isUserAChannelMemeber();
      //     })
      //     .catch(() => {
      //       console.log('Channel does not yet exist');
      //       this.createChannel();
      //     })
      // },
      // isUserAChannelMemeber() {
      //   this.chatClient.getSubscribedChannels()
      //     .then(channels => {
      //       if (channels.items != 0) {
      //         if (this.channel.uniqueName == channels.items[0].state.uniqueName) {
      //           console.log('Already a member of ' + this.channelFriendlyName);
      //           this.getChannelMessages()
      //         } else {
      //           console.log('Not yet a member of ' + this.channelFriendlyName);
      //           this.joinChannel(this.channel);
      //         }
      //       } else {
      //         this.joinChannel(this.channel);
      //       }
      //     });
      // },
      // joinChannel() {
      //   this.channel.join()
      //     .then((channel) => {
      //       console.log('Joined channel: ' + channel.friendlyName);
      //       this.getChannelMessages();
      //     });
      // },
      // createChannel() {
      //   this.chatClient.createChannel({
      //     uniqueName: this.channelUniqueName,
      //     friendlyName: this.channelFriendlyName
      //   })
      //     .then(channel => {
      //       console.log('Created new channel: ' + channel.friendlyName);
      //       this.channel = channel;
      //       this.joinChannel();
      //     });
      // },
      createChatClient() {
        Chat.Client.create(this.user.auth_token)
        .then((client) => {
          this.chatClient = client;
          // this.doesChannelExist(this.channelUniqueName);
          this.getChannels();
        })
        .catch(error => {
          console.log(error.message);
          if (error.message.toLowerCase().includes('access token expired')) {
            console.log('YUP!');
            //TODO: call refresh token route
          }
        });
      },
      getChannels() {
        this.chatClient.getSubscribedChannels()
          .then(channels => {
            this.channels = channels.items;
            this.selectedChannel = this.channels[0];
            console.log('fetched subscribed channels');
          })
      },
      onSelectedChannel(channel) {
        console.log('selected channel');
        this.selectedChannel = channel;
      }
    },
    created() {
      this.createChatClient();
    }
}
</script>

<style>
</style>
