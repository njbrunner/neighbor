<template>
<div>
  <h1>Chat</h1>
  {{ user }}
</div>
</template>

<script>
export default {
    name: 'Chat',
    props: {
        user: String
    }
}
</script>

<style>

</style>
