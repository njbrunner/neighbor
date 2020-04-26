<template>
<div>
  <div
    class="message"
    :class="isMessageOwned ? 'message-owned' : 'message-not-owned'">
    <p class="message-timestamp">{{ message.timestamp }}</p>
    <div class="message-text-container">
      <p class="message-text add-shadow">{{ message.body }}</p>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: "Message",
  props: {
    message: Object,
    user: Object
  },
  computed: {
    isMessageOwned() {
      return (this.message.author == this.user.unique_identity)
    }
  }
};
</script>

<style>
.message-timestamp {
  color: grey;
}

.message > .message-timestamp {
  margin-bottom: 0;
}

.message-text {
  display: inline-block;
  padding: 10px 15px;
  border-radius: 10px;
  max-width: 75%;
}

.message-owned > .message-text-container > .message-text {
  border: 1px solid lightgrey;
  text-align: left;
}

.message-owned {
  text-align: right;
}

.message-not-owned > .message-text-container > .message-text {
  color: white;
  background: red;
}

.add-shadow {
  box-shadow: 2px 4px 4px 0px rgba(0, 0, 0, 0.19);
}
</style>
