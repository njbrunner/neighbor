<template>
  <div
    class="channel-wrapper"
    @click="selectChannel">
    <div class="channel">
    {{ channel.friendlyName }}
    </div>
  </div>
</template>

<script>
export default {
    name: "Channel",
    props: {
        channel: Object
    },
    methods: {
        selectChannel() {
            this.$emit('onSelectedChannel', this.channel);
        }
    }
}
</script>

<style>
.channel-wrapper {
    border: solid 1px lightgrey;
    border-radius: 5px;
    box-shadow: 4px 4px 4px rgba(0, 0, 0, .19);
    padding: 15px;
    cursor: pointer;
}

.channel {
    border-right: 4px solid red;
    padding: 15px;
}
</style>
