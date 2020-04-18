<template>
  <div class="home">
    <h1>Home Page</h1>
    <div>
      {{ user.latitude }}
      {{ user.longitude }}
    </div>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      roleDefined: true
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
      })
    },
    errorLocation() {
      console.log('Unable to retrieve your location');
      this.$toasted.show('Unable to retrieve your location');
    },
    checkLocation() {
      if(!this.user.latitude || !this.user.longitude) {
        console.log('getLocation');
        this.getlocation();
      }
    }
  },
  created() {
    this.checkLocation();
    console.log('created');
  },
  beforeUpdate() {
    this.checkLocation();
    console.log('upated');
  }
}
</script>
