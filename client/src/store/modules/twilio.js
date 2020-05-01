const Chat = require('twilio-chat');

const state = {
  chatClient: undefined
};

const getters = {
  getChatClient: state => state.chatClient
};

const actions = {
  createChatClient({ commit }, twilio_token) {
    Chat.Client.create(twilio_token)
      .then(client => {
        client.on('channelInvited', channel => channel.join());
        commit('updateChatClient', client);
      })
      .catch(error => {
        console.log(error);
        this._vm.$toasted.show(error.message);
      });
  },
};

const mutations = {
  updateChatClient: (state, client) => {
    state.chatClient = client;
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};
