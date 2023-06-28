<template>
    <div>
        <!-- Page content -->
        <CustomNavBar/>
        <main>
          <nuxt />
        </main>
    </div>
</template>

<script>
import CustomNavBar from '../components/CustomNavBar.vue'

export default {
    middleware: 'auth',
    components: {
        CustomNavBar
    }
}
</script>