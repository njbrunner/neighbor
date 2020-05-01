<template>
<div class="potential-neighbor-card">
    <h4 class="card-name">{{ potentialNeighbor.name }}</h4>
    <v-btn
      class="button-chat"
     color="primary"
     rounded
     outlined
     @click="createChat">
     Chat
    </v-btn>
</div>
</template>

<script>
export default {
    name: 'PotentialNeighbor',
    props: {
        potentialNeighbor: Object,
        user: Object
    },
    computed: {
      uniqueChannelName() {
        if (this.user.id < this.potentialNeighbor.id) {
          return this.user.id + '_' + this.potentialNeighbor.id;
        } else {
          return this.potentialNeighbor.id + '_' + this.user.id;
        }
      }
    },
    methods: {
      createChat() {
        this.$emit(
          'onCreateChat',
          {
            'uniqueChannelName': this.uniqueChannelName,
            'potentialNeighborUniqueIdentity': this.potentialNeighbor.id,
            'potentialNeighborName': this.potentialNeighbor.name
          }
        );
      }
    }
}
</script>

<style>
.potential-neighbor-card {
    border: solid 1px lightgrey;
    border-radius: 5px;
    box-shadow: 2px 2px 4px rgba(0, 0, 0, .19);
    max-width: 400px;
    padding: 15px;
    margin: 15px auto;
    display: flex;
    flex-direction: row;
}

.card-name {
  flex: 1;
}

.button-chat {

}
</style>
