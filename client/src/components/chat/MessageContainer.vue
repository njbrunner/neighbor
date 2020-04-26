<template>
  <v-container
    class="message-container"
    v-scroll
    id="test"
    ref="test">
    <Message
      v-for="(message, index) in messages"
      :key="index"
      :message="message"
      :user="user">
    </Message>
  </v-container>
</template>

<script>
import Message from '@/components/chat/Message';

export default {
    name: 'MessageContainer',
    props: {
      messages: Array,
      user: Object,
    },
    components: {
      Message
    },
    created() {
      
    }
}
</script>

<style>
.message-container {
  overflow-y: scroll;
  margin-bottom: 100px;
  /* flex: 1; */
  /* max-height: calc(100vh - ); */
}
