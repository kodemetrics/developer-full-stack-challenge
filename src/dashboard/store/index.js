export const state = () =>({
    books: [],
    authors: [],
    user: localStorage.getItem('USER'),
    token: localStorage.getItem('TOKEN'),
    isLoggedIn: localStorage.getItem('TOKEN') ? true : false,
})


export const mutations = {
    LOGGED_IN(state,isActive){
        state.isLoggedIn = isActive;
    },
    LOG_OUT(state){
        state.isLoggedIn = false;
    },

    SET_USER(state,payload){
        const {username, password} = payload;
        state.user = username;
        localStorage.setItem('USER', username)
    },
    DELETE_USER(state){
        state.user = null;
        localStorage.removeItem('USER')
    },

    SET_TOKEN(state,newToken){
        state.token = newToken;
        localStorage.setItem('TOKEN', newToken)
    },
    DELETE_TOKEN(state){
        state.token = null;
        localStorage.removeItem('TOKEN')
    }
}


export const getters = {
  isAuthenticated(state) {
    // return state.auth.loggedIn
     return state.isLoggedIn
  },

  loggedInUser(state) {
    //return state.auth.user
     return state.user 
  }
}

