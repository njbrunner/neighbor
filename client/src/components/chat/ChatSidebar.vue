<template>
  <div class="sidebar">
    <div class="channel-container">
      <Channel
        v-for="(channel, index) in channels"
        :key="index"
        :channel="channel"
        :user="user"
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
    methods: {
      onSelectedChannel(channelData) {
        this.$emit('onSelectedChannel', channelData);
      }
    }
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
