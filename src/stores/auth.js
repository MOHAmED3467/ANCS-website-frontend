import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  // ── State ──
  const token    = ref(localStorage.getItem('token')         || '')
  const username = ref(localStorage.getItem('dash-username') || '')
  const role     = ref(localStorage.getItem('dash-role')     || '')

  // ── Getters ──
  const isLoggedIn = computed(() => !!token.value)
  const isAdmin    = computed(() => role.value === 'admin')
  const isUser     = computed(() => role.value === 'user')

  // ── Actions ──
  function loginSuccess(accessToken, user, userRole) {
    token.value    = accessToken
    username.value = user     || 'User'
    role.value     = userRole || 'user'

    localStorage.setItem('token',         accessToken)
    localStorage.setItem('dash-username', user     || 'User')
    localStorage.setItem('dash-role',     userRole || 'user')
  }

  function logout() {
    token.value    = ''
    username.value = ''
    role.value     = ''
    localStorage.removeItem('token')
    localStorage.removeItem('dash-username')
    localStorage.removeItem('dash-role')
  }

  return { token, username, role, isLoggedIn, isAdmin, isUser, loginSuccess, logout }
})
