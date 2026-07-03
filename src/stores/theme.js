import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useThemeStore = defineStore('theme', () => {
  const isDark = ref(localStorage.getItem('ancs-theme') !== 'light')

  const theme = computed(() => isDark.value ? 'dark' : 'light')

  function toggle() {
    isDark.value = !isDark.value
    localStorage.setItem('ancs-theme', isDark.value ? 'dark' : 'light')
    applyTheme()
  }

  function applyTheme() {
    document.documentElement.setAttribute('data-theme', isDark.value ? 'dark' : 'light')
  }

  // Apply on init
  applyTheme()

  return { isDark, theme, toggle, applyTheme }
})
