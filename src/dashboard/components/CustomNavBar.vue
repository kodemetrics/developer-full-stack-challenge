<template>
    <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="#">NavBar</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
       
            <b-navbar-nav>
              <nuxt-link class="nav-link" to="/login">Login</nuxt-link>
            </b-navbar-nav>

        </b-collapse>
      </b-navbar>
</template>
