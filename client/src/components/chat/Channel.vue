<template>
  <div class="channel-wrapper" @click="selectChannel">
    <div class="channel">{{ channelDisplayName }}</div>
  </div>
</template>

<script>
export default {
  name: "Channel",
  props: {
    channel: Object,
    user: Object
  },
  computed: {
    channelDisplayName() {
      let displayNames = this.channel.attributes.displayNames;
      if (displayNames[0] == this.user.name) {
          return displayNames[1];
      }
      return displayNames[0]
    }
  },
  methods: {
    selectChannel() {
      this.$emit(
        "onSelectedChannel",
        {
          'channel': this.channel,
          'channelDisplayName': this.channelDisplayName
        }
      );
    },
  }
};
</script>

<style>
.channel-wrapper {
  border: solid 1px lightgrey;
  border-radius: 5px;
  box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.19);
  padding: 15px;
  cursor: pointer;
  margin-bottom: 15px;
}

.channel {
  border-right: 4px solid red;
  padding: 15px;
}
</style>
