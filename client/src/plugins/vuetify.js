import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import colors from 'vuetify/lib/util/colors';

import '@mdi/font/css/materialdesignicons.css';


Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    options: {
      customProperties: true,
    },
    themes: {
      light: {
        primary: '#ff0000',
        background: colors.white,
      },
    },
  },
  icons: {
    iconfont: 'mdi',
  },
});
