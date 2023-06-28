export default {
    // Disable server-side rendering: https://go.nuxtjs.dev/ssr-mode
    ssr: false,

    // Target: https://go.nuxtjs.dev/config-target
    target: 'static',

    // Global page headers: https://go.nuxtjs.dev/config-head
    head: {
        title: 'DC Full Stack Code Challenge',
        htmlAttrs: {
            lang: 'en',
        },
        meta: [
            { charset: 'utf-8' },
            {
                name: 'viewport',
                content: 'width=device-width, initial-scale=1',
            },
            { hid: 'description', name: 'description', content: '' },
            { name: 'format-detection', content: 'telephone=no' },
        ],
        link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
    },

    // Global CSS: https://go.nuxtjs.dev/config-css
    css: [],

    // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
    plugins: [],

    // Auto import components: https://go.nuxtjs.dev/config-components
    components: true,

    // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
    buildModules: [
        // https://go.nuxtjs.dev/typescript
        '@nuxt/typescript-build',
    ],

    // Modules: https://go.nuxtjs.dev/config-modules
    modules: [
        // https://go.nuxtjs.dev/bootstrap
        ['bootstrap-vue/nuxt', { icons: true, css: true }],
        // https://go.nuxtjs.dev/axios
        '@nuxtjs/axios',
        '@nuxtjs/auth',  
        '@nuxtjs/toast',
        '@nuxtjs/dotenv',
    ],

    publicRuntimeConfig: {
        axios: {
            baseURL: process.env.BASEURL || 'http://127.0.0.1:8100',
        },
    },

    // Axios module configuration: https://go.nuxtjs.dev/config-axios
    axios: {
        // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
        baseURL: process.env.NODE_ENV == 'development' ? 'http://127.0.0.1:8100' : process.env.BASEURL,
    },

    auth: {
        strategies: {
            local: {
                token: {
                    property: 'token',
                    global: true,
                    required: true,
                    name:'Authorization',
                    type: 'Bearer'
                },
                user: {
                    property: 'user',
                    // autoFetch: true
                },
                endpoints: {
                    login: { url: 'api/v1/login', method: 'post', propertyName: 'token' },
                    // user: { url: 'api/v1/users/', method: 'get', propertyName: 'data' },
                    // post_authors: { url: 'api/v1/authors/create', method: 'post', propertyName: 'data' },
                    // authors: { url: 'api/v1/authors/', method: 'get', propertyName: 'data' },
                    //authors: { url: 'api/v1/authors/', method: 'get', propertyName: 'data.token' },
                    user: false,
                    logout: false
                }
            }
        }
    },

    // Build Configuration: https://go.nuxtjs.dev/config-build
    build: {},
};
