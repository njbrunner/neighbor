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
        if (this.user.unique_identity < this.potentialNeighbor.unique_identity) {
          return this.user.unique_identity + '_' + this.potentialNeighbor.unique_identity;
        } else {
          return this.potentialNeighbor.unique_identity + '_' + this.user.unique_identity;
        }
      }
    },
    methods: {
      createChat() {
        this.$emit(
          'onCreateChat',
          {
            'uniqueChannelName': this.uniqueChannelName,
            'potentialNeighborUniqueIdentity': this.potentialNeighbor.unique_identity,
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
