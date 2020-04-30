<template>
<div>
  <v-row>
    <v-col
      :cols="3">
      <ChatSidebar
        :channels="channels"
        :user="user"
        @onSelectedChannel="onSelectedChannel">
      </ChatSidebar>
    </v-col>
    <v-col
      :cols="9">
      <MessageContainer
        :user="user"
        :selectedChannel="selectedChannel"
        :selectedChannelDisplayName="selectedChannelDisplayName">
      </MessageContainer>
    </v-col>
  </v-row>
</div>
</template>

<script>
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
        channels: undefined,
        selectedChannel: undefined,
        selectedChannelDisplayName: undefined
      }
    },
    computed: {
      chatClient() {
        return this.$store.getters.getChatClient;
      }
    },
    methods: {
      getChannels() {
        this.chatClient.getSubscribedChannels()
          .then(channels => {
            this.channels = channels.items;
            this.selectedChannel = this.channels[0];
            this.selectedChannelDisplayName = this.getChannelDisplayName(this.channels[0]);
          })
      },
      getChannelDisplayName(channel) {
        let displayNames = channel.attributes.displayNames;
        if (displayNames[0] == this.user.name) {
            return displayNames[1];
        }
        return displayNames[0]
      },
      onSelectedChannel(channelData) {
        this.selectedChannel = channelData.channel;
        this.selectedChannelDisplayName = channelData.channelDisplayName;
      }
    },
    created() {
      this.getChannels();
    }
}
</script>

<style>
</style>
