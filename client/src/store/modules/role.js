import axios from 'axios';

const state = {
    roles: undefined
};

const getters = {
    getRoles: state => state.roles
};

const actions = {
    getRoles({commit}) {
        return new Promise((resolve, reject) => {
            axios({
                url: 'https://covid-19-hackathon-app.herokuapp.com/role/',
                method: 'GET'
            })
            .then(response => {
                commit('updateRoles', response.data.roles);
                resolve(response);
            })
            .catch(error => {
                reject(error);
            });
        });
    }
};

const mutations = {
    updateRoles: (state, roles) => {
        state.roles = roles;
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};
