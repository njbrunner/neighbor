<template>
  <div class="channel-container">
    <Channel
      v-for="(channel, index) in channels"
      :key="index"
      :channel="channel"
      @onSelectedChannel="onSelectedChannel">
    </Channel>
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
      channels: Array
    },
    methods: {
      onSelectedChannel(channel) {
        this.$emit('onSelectedChannel', channel);
      }
    }
}
</script>

<style>
</style>
