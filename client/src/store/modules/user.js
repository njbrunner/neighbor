import axios from 'axios';
import jwt from 'jsonwebtoken';
import router from '../../router';
import store from '../../store';


const state = {
    user: undefined,
    token: undefined,
    refresh: undefined,
    potentialNeighbors: undefined
};

const getters = {
    getUser: state => state.user,
    isLoggedIn: state => !!state.user,
    getToken: state => state.token,
    getRefreshToken: state => state.refreshToken,
    getPotentialNeighbors: state => state.potentialNeighbors
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
                commit('updateUser', response.data.user);
                commit('updateRefresh', response.data.refresh);
                commit('updateToken', response.data.token);
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
                commit('updateUser', response.data.user);
                commit('updateRefresh', response.data.refresh);
                commit('updateToken', response.data.token);
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
    updateUser({ commit }, userData) {
        commit('updateUser', userData);
    },
    updateLocation({ commit}, userLocationData) {
        const locationData = {
            'latitude': userLocationData.latitude,
            'longitude': userLocationData.longitude
        }
        return new Promise((resolve, reject) => {
            axios({
                url: 'http://127.0.0.1:8000/user/' + state.user.id,
                data: locationData,
                method: "PATCH"
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
    fetchPotentialNeighbors({ commit }) {
        axios({
            url: 'http://127.0.0.1:8000/user/nearby/' + state.user.id,
            method: 'GET'
        })
        .then(response => {
            commit('updatePotentialNeighbors', response.data);
        })
        .catch(error => {
            console.log(error);
        });
    }
};

const mutations = {
    updateUser: (state, userData) => {
        state.user = userData;
        if (state.user) {
            localStorage.setItem('user', JSON.stringify(userData));
        }
    },
    updatePotentialNeighbors(state, potentialNeighbors) {
        state.potentialNeighbors = potentialNeighbors;
    },
    logout: (state) => {
        state.user = undefined;
        state.potentialNeighbors = undefined;
    },
    updateToken: (state, token) => {
        state.token = token;
        updateAuthBearer();
    },
    updateRefresh: (state, refresh) => {
        state.refresh = refresh;
    }
};


var authTokenRequest = null;

function getAuthToken () {
  // if the current store token expires soon
  if (jwt.decode(store.getters['getToken']).exp - 240 <= (Date.now() / 1000).toFixed(0)) {
  // if not already requesting a token
  if (authTokenRequest === null) {
    console.log("in refresh token block");
    authTokenRequest = //axios.post('/refresh-token', {}, { withCredentials: true })
      axios({
          url: 'http://127.0.0.1:8000/refresh-token',
          data: {},
          method: 'GET',
          config: { withCredentials: true }
      })
      .then(response => {
        // request complete and store
        resetAuthTokenRequest()
        store.commit('updateRefresh', response.data.access_token)
        return response.data.access_token
      })
    }
    return authTokenRequest
  }
  return store.getters['getToken']
}

// tokenRequest dirty bit reseter
function resetAuthTokenRequest () {
  authTokenRequest = null
}

function updateAuthBearer () {
  // Axios Intercept Requests
  axios.interceptors.request.use(async function (config) {
    // If not one of these specific pages that doesn't need a token, use method to get the current token or request a new one.  Otherwise, use current token (possibly none)
    if (config.url.includes('twilio')){
      config.headers['Authorization'] = 'Bearer ' + store.getters['getUser'].twilio_token
    } else if (!config.url.includes('login') && !config.url.includes('refresh-token') && !config.url.includes('signup')) {
      config.headers['Authorization'] = 'Bearer ' + await getAuthToken()
    } else {
      console.log("Used refresh token for " + config.url);
      config.headers['Authorization'] = 'Bearer ' + store.getters['getRefreshToken']
    }
    return config
  }, function (error) {
    console.log("Error in interceptor" + error);
    return Promise.reject(error)
  })
  
  axios.interceptors.response.use(function (config) {
    return config
  }, function (error) {
    console.log("Error in interceptor" + error);
    // Prevent endless redirects (login is where you should end up)
    if (error.request !== undefined) {
      if (error.request.responseURL.includes('login')) {
        return Promise.reject(error)
      }
    }
  
    // If you can't refresh your token or you are sent Unauthorized on any request, logout and go to login
    if (error.request !== undefined && (error.request.responseURL.includes('refresh') || error.request.status === 401 && error.config.__isRetryRequest)) {
      store.dispatch('logout')
      router.push({name: 'Login'})
    } else if (error.request !== undefined && error.request.status === 401) {
      error.config.__isRetryRequest = true
      return axios.request(error.config)
    }
    return Promise.reject(error)
  })
}


export default {
    state,
    getters,
    actions,
    mutations
};
