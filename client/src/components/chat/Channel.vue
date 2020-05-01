<template>
  <div
    class="channel-wrapper"
    @click="selectChannel"
    :class="{activeChannel: isActiveChannel}">
    <div
      class="channel"
      :class="{newChannel: isNewChannel}">{{ channelDisplayName }}
    </div>
  </div>
</template>

<script>
export default {
  name: "Channel",
  props: {
    channel: Object,
    user: Object,
    selectedChannel: Object
  },
  computed: {
    channelDisplayName() {
      let displayNames = this.channel.attributes.displayNames;
      if (displayNames[0] == this.user.name) {
          return displayNames[1];
      }
      return displayNames[0]
    },
    newInvitations() {
      return this.$store.getters.getNewInvitations;
    },
    isNewChannel() {
      return this.newInvitations.includes(this.channel.uniqueName);
    },
    isActiveChannel() {
      if (this.selectedChannel) {
        return this.selectedChannel == this.channel;
      }
      return false;
    }
  },
  methods: {
    selectChannel() {
      this.$emit("onSelectedChannel", this.channel);
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
  padding: 15px;
}
.newChannel {
  border-right: 4px solid red;
}
.activeChannel {
  border: solid 1px red;
  font-weight: bold;
  color: red;
}
</style>
