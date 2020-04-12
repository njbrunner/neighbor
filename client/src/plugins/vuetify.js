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
        primary: colors.blue.lighten4, // #B3E5FC
        background: colors.grey.lighten5,
      },
    },
  },
  icons: {
    iconfont: 'mdi',
  },
});
