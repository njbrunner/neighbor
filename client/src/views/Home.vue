<template>
  <div class="home">
    <h1>Home Page</h1>
    <v-btn @click="goToChat">Chat</v-btn>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      chatUser: undefined
    }
  },
  computed: {
    user() {
      return this.$store.getters.getUser;
    }
  },
  methods: {
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
        console.log('denied');
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
      if(!this.user.latitude || !this.user.longitude) {
        this.getlocation();
      }
    },
    goToChat() {
      this.$router.push({name: 'Chat', params: {user: this.user}});
    }
  },
  created() {
    this.checkLocation();
  },
  beforeUpdate() {
    this.checkLocation();
  }
}
</script>
