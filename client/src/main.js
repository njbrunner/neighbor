import Vue from 'vue';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';
import store from './store';
import Toasted from 'vue-toasted';

const toasted_options = {
  "position": "bottom-right",
  "theme": "bubble",
  "duration": 3000,
  "keepOnHover": true
};
Vue.use(Toasted, toasted_options);

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  vuetify,
  router,
  store
}).$mount('#app');
