<template>
  <div class="home">
    <v-container class="potential-neighbors-container">
      <h1 class="primary--text">Potential Neighbors</h1>
      <hr>
      <PotentialNeighbor
        v-for="(potentialNeighbor, index) in potentialNeighbors"
        :key="index"
        :potentialNeighbor="potentialNeighbor"
        :user="user"
        @onCreateChat="onCreateChat">
      </PotentialNeighbor>
    </v-container>
  </div>
</template>

<script>
import PotentialNeighbor from '@/components/PotentialNeighbor';

export default {
  name: 'Home',
  components: {
    PotentialNeighbor
  },
  props: {
    user: Object
  },
  data() {
    return {
      chatUser: undefined
    }
  },
  computed: {
    potentialNeighbors() {
      return this.$store.getters.getPotentialNeighbors;
    },
    chatClient() {
      return this.$store.getters.getChatClient;
    }
  },
  watch: {
    user() {
      if (this.user.location_identified) {
        this.$store.dispatch('fetchPotentialNeighbors');
      }
    }
  },
  methods: {
    onCreateChat(newChannelData) {
      this.doesChannelExist(newChannelData)
    },
    doesChannelExist(newChannelData) {
      this.chatClient.getChannelByUniqueName(newChannelData.uniqueChannelName)
        .then(channel => {
          this.joinChannel(channel);
        })
        .catch(() => {
          this.createChannel(newChannelData);
        })
    },
    joinChannel(channel, potentialNeighborUniqueIdentity) {
      channel.join()
        .then(() => {
          channel.invite(potentialNeighborUniqueIdentity)
            .then(() => {
              this.$router.push({name: 'Chat'});
            })
        });
    },
    createChannel(newChannelData) {
      this.chatClient.createChannel(
        {
          uniqueName: newChannelData.uniqueChannelName,
          attributes: {
            displayNames: [this.user.name, newChannelData.potentialNeighborName]
          }
        }
      )
        .then(channel => {
          this.joinChannel(channel, newChannelData.potentialNeighborUniqueIdentity);
        });
    },
    getlocation() {
      if (!navigator.geolocation) {
        console.log('Geolocation is not supported by your browser');
        this.$toasted.show('Geolocation is not supported by your browser');
      } else {
        navigator.geolocation.getCurrentPosition(this.successLocation, this.errorLocation);
      }
    },
    successLocation(position) {
      const userLocationData = {
        'userId': this.user.id,
        'latitude': position.coords.latitude,
        'longitude': position.coords.longitude
      }
      this.$store.dispatch(
        'updateLocation',
        userLocationData
      )
      .then(response => {
        this.$store.dispatch('updateUser', response.data);
      })
      .catch(error => {
        console.log(error);
        this.$toasted.show(error.message);
      })
    },
    errorLocation(error) {
      if (error.code == error.PERMISSION_DENIED) {
        alert('This application needs to access your location data in order to pair you with ' +
         'other users that either need help or can provide help. We will not share your location ' +
         'with anyone.\n\n' +
         'Please enable Location Permissions in your browser before selecting OK.');
        this.getlocation();
      } else {
        this.$toasted.show('Unable to retrieve your location');
      }
    },
    checkLocation() {
      if(!this.user.location_identified) {
        this.getlocation();
      }
    },
  },
  created() {
    if (!this.user.location_identified) {
      this.getlocation();
    } else {
      this.$store.dispatch('fetchPotentialNeighbors');
      this.$store.dispatch('createChatClient', this.user.auth_token);
    }
  },
  beforeUpdate() {
    this.checkLocation();
  }
}
</script>
<style>
.potential-neighbors-container {
  max-width: 800px;
  align-content: center;
}
</style>
