import './assets/main.css'

import { createApp }    from 'vue'
import { createPinia }  from 'pinia'
import App              from './App.vue'
import router           from './router'
import { useThemeStore } from './stores/theme'
import './theme.css'

const pinia = createPinia()
const app   = createApp(App)

app.use(pinia)

// Initialize theme before rendering
const themeStore = useThemeStore()
themeStore.applyTheme()

app.use(router)
app.mount('#app')
