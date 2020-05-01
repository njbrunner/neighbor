<template>
  <div class="sidebar">
    <div class="channel-container">
      <Channel
        v-for="(channel, index) in channels"
        :key="index"
        :channel="channel"
        :user="user"
        :selectedChannel="selectedChannel"
        @onSelectedChannel="onSelectedChannel">
      </Channel>
    </div>
    <div class="sidebar-spacer"></div>
  </div>

</template>

<script>
import Channel from '@/components/chat/Channel';

export default {
    name: "ChatSidebar",
    components: {
      Channel
    },
    props: {
      channels: Array,
      user: Object
    },
    watch: {
      channels() {
        if (this.channels != undefined && this.selectedChannel == undefined) {
          this.onSelectedChannel(this.channels[0]);
        }
      }
    },
    data() {
      return {
        selectedChannel: undefined
      }
    },
    computed: {
      newInvitations() {
        return this.$store.getters.getNewInvitations;
      }
    },
    methods: {
      onSelectedChannel(channel) {
        if(this.newInvitations.includes(channel.uniqueName)){
          this.$store.commit('removeNewInvitation', channel.uniqueName);
        }

        let channelData = {
          channel: channel,
          channelDisplayName: this.channelDisplayName(channel)
        };
        this.selectedChannel = channel;
        this.$emit('onSelectedChannel', channelData);
      },
      channelDisplayName(channel) {
        let displayNames = channel.attributes.displayNames;
        if (displayNames[0] == this.user.name) {
            return displayNames[1];
        }
        return displayNames[0]
      },
    },
}
</script>

<style>
.sidebar {
  display: flex;
  flex-direction: column;
  height: calc(100vh - 100px);
}
.channel-container {
  height: 100%;
  border-right: solid 2px red;
  padding: 15px 30px 15px 0px;
  display: flex;
  flex-direction: column;
  flex: 1;
  overflow-y: scroll;
}
.sidebar-spacer {
  margin-top: 15px;
}
</style>
