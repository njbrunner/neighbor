import Vue from 'vue';
import Vuex from 'vuex';

import role from '@/store/modules/role';
import user from '@/store/modules/user';
import twilio from '@/store/modules/twilio';

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        role,
        user,
        twilio
    }
});
