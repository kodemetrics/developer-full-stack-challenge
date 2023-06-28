<template>
    <section class="section">
        <div class="container">
            <div class="columns">
                <div class="column is-4 is-offset-4">
                    <h2 class="title has-text-centered">Welcome back!</h2>

                    <Notification :message="error" v-if="error" />

                    <form method="post" @submit.prevent="login">
                        <div class="field">
                            <label class="label">Username</label>
                            <div class="control">
                                <input type="text" class="input" name="username" v-model="username"/>
                            </div>
                        </div>
                        <div class="field">
                            <label class="label">Password</label>
                            <div class="control">
                                <input type="password" class="input" name="password" v-model="password"/>
                            </div>
                        </div>
                        <div class="control">
                            <button type="submit" class="button is-dark is-fullwidth">Log In</button>
                        </div>
                    </form>
                    <div class="has-text-centered" style="margin-top: 20px">
                        <p>
                            Don't have an account? <nuxt-link to="/register">Register</nuxt-link>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import Notification from '~/components/Notification'
import axios from "axios"

export default {
    layout: 'custom', // Specify the layout file
    components: {
        Notification,
    },

    data() {
        return {
            username: 'John',
            password: 'Doe',
            error: null
        }
    },

    methods: {
        login(){
            var header = {'Accept': 'application/json','Content-Type': 'application/json;charset=utf-8' };
            var data = {"username":this.username,"password":this.password};
            const url =  process.env.BASEURL + "login";
            console.log(url);
            var result = axios.post(url,data,header).then((response) => {

                      var payload = response.data.data;
                      var token = response.data.token;
                      //const { username, password } = payload;
                    
                      this.$store.commit('LOGGED_IN', true);
                      this.$store.commit('SET_USER', payload);
                      this.$store.commit('SET_TOKEN', token);
                      this.$router.push('/')

                      //console.log(response.data);
                      //console.log(response.data.data.username);
                      //console.log(username +"  "+ password);
                      //console.log(token);
                     
            }).catch((response) => {
                      console.log(response);
                      alert("Invalid credentails");
            });
        },

        /*
        async login() {
            try {
              await this.$auth.loginWith('local', {
                    data: {
                        username: this.username,
                        password: this.password
                    }
                }).catch(e => {
                    this.$toast.error('Failed Logging In', { icon: "error_outline" });
                });
            //  await this.$axios.post('login', {
            //         username: this.username,
            //         password: this.password
            //     })
                // console.log(response);
                // console.log(this.$auth.token);

                if (this.$auth.loggedIn) {
                    this.$toast.success('Successfully Logged In', { icon: "done" });
                    const token = this.$auth.getToken('local');

                    // this.$store.state.isLoggedIn = true;
                    this.$store.commit('LOGGED_IN', true);
                    this.$store.commit('SET_TOKEN', token);

                    console.log(token);
                    this.$router.push('/')
                }
              
            } catch (e) {
                // this.error = e.response.data.message
                this.error = e.response.data
                console.log(this.error);
            }
           
        }
         */
    }
}
</script>