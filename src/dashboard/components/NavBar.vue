<template>
    <!-- <nav class="navbar is-light">
        <div class="container">
            <div class="navbar-brand">
                <nuxt-link class="navbar-item" to="/">Nuxt Auth</nuxt-link>
                <button class="button navbar-burger">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>
            <div class="navbar-menu">
                <div class="navbar-end">
                    <div class="navbar-item has-dropdown is-hoverable">
                        <a class="navbar-link">
                            My Account
                        </a>
                        <div class="navbar-dropdown">
                            <nuxt-link class="navbar-item" to="/profile">My Profile</nuxt-link>
                            <hr class="navbar-divider" />
                            <a class="navbar-item">Logout</a>
                        </div>
                    </div>
                    <template>
                        <nuxt-link class="navbar-item" to="/register">Register</nuxt-link>
                        <nuxt-link class="navbar-item" to="/login">Log In</nuxt-link>
                    </template>
                </div>
            </div>
        </div>
    </nav> -->


<!-- <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <nuxt-link class="navbar-brand" to="/">Navbar</nuxt-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
             <nuxt-link class="nav-link" to="/">Home <span class="sr-only">(current)</span></nuxt-link>
          </li>

          <li class="nav-item">
                 <nuxt-link class="nav-link" to="/authors">Authors</nuxt-link>
          </li>

          <li class="nav-item">
                 <nuxt-link class="nav-link" to="/books">Books</nuxt-link>
         </li>
          <li class="nav-item">
             <nuxt-link class="nav-link" to="/register">Register</nuxt-link>
          </li>
          <li class="nav-item">
             <nuxt-link class="nav-link" to="/login">Login</nuxt-link>
          </li>
        </ul>
      </div>
    </nav> -->


    <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="#">NavBar</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav v-if="isAuthenticated">
            <nuxt-link class="nav-link" to="/">Home</nuxt-link>
            <nuxt-link class="nav-link" to="/authors">Authors</nuxt-link>
            <nuxt-link class="nav-link" to="/books">Books</nuxt-link>
            <!-- <nuxt-link @click.prevent="logout" class="nav-link" to="#">Logout</nuxt-link> -->
            <a class="nav-link" @click="logout">Logout</a>
          </b-navbar-nav>

            <!-- <b-navbar-nav v-else>
              <nuxt-link class="nav-link" to="/login">Login</nuxt-link>
            </b-navbar-nav> -->

        
        </b-collapse>
      </b-navbar>
</template>


<script>
  import { mapGetters } from 'vuex'
  export default {
  computed: {
    ...mapGetters(['isAuthenticated', 'loggedInUser'])
  },
  methods: {
     logout(){
      event.preventDefault();

      this.$auth.logout()
        .then(() => {
         
          this.$store.commit("LOGGED_OUT");
          this.$store.commit("DELETE_TOKEN");
          this.$store.commit("DELETE_USER");
          console.log("Logged Out");

          // Optional: Redirect the user to a specific page after successful logout
          this.$router.push('/login');
        })
        .catch((error) => {
          console.error('Logout error:', error);
        });
       
    },

   }
}

</script>