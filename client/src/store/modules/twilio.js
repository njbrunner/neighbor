const Chat = require('twilio-chat');

const state = {
  chatClient: undefined,
  newInvitations: []
};

const getters = {
  getChatClient: state => state.chatClient,
  getNewInvitations: state => state.newInvitations
};

const actions = {
  createChatClient({ commit }, twilio_token) {
    Chat.Client.create(twilio_token)
      .then(client => {
        client.on('channelInvited', channel => {
          channel.join();
          commit('addNewInvitation', channel.uniqueName);
        });
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
  },
  addNewInvitation: (state, channelName) => {
    state.newInvitations.push(channelName);
  },
  removeNewInvitation: (state, channelName) => {
    let index = state.newInvitations.indexOf(channelName);
    if (index !== -1) {
      state.newInvitations.splice(index, 1);
    }
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};
