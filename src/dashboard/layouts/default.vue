<template>
    <div>
        <!-- Common header -->
        <Navbar />

        
        <!-- Page content -->
        <main>
          <nuxt />
        </main>
    </div>
</template>

<script>
import Navbar from '../components/NavBar.vue'

export default {
    middleware: 'guest',
    components: {
        Navbar
    }
}
</script>