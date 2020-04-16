import axios from 'axios';

const state = {
    user: undefined
};

const getters = {
    getUser: state => state.user,
    isLoggedIn: state => !!state.user
};

const actions = {
    signup({ commit }, userData) {
        return new Promise((resolve, reject) => {
            axios({
                url: 'http://127.0.0.1:8000/user/signup',
                data: userData,
                method: 'POST'
            })
            .then(response => {
                commit('updateUser', response.data);
                resolve(response);
            })
            .catch(error => {
                reject(error);
            });
        });
    },
    login({ commit }, loginData) {
        return new Promise((resolve, reject) => {
            axios({
                url: 'http://127.0.0.1:8000/user/login',
                data: loginData,
                method: 'POST'
            })
            .then(response => {
                commit('updateUser', response.data);
                resolve(response);
            })
            .catch(error => {
                reject(error);
            });
        });
    },
    logout({ commit }) {
        localStorage.removeItem('user');
        commit('logout');
    },
    fetchUser({ commit }) {
        var storedUser = JSON.parse(localStorage.getItem('user'));
        if (!storedUser) {
            storedUser = undefined;
        }
        commit('updateUser', storedUser);
    },
};

const mutations = {
    updateUser: (state, userData) => {
        state.user = userData;
        if (state.user) {
            localStorage.setItem('user', JSON.stringify(userData));
        }
    },
    logout: (state) => {
        state.user = undefined;
    }
};

export default {
    state,
    getters,
    actions,
    mutations
};
