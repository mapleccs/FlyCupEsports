import { defineStore } from 'pinia'
import { fetchMatches, fetchTeams, fetchTournaments } from '@/services/scheduleService'

export const useScheduleStore = defineStore('schedule', {
  state: () => ({
    matches: [],
    teams: [],
    tournaments: [],
    loading: false,
    error: null
  }),
  actions: {
    async fetchScheduleData() {
      this.loading = true
      try {
        const [matches, teams, tournaments] = await Promise.all([
          fetchMatches(),
          fetchTeams(),
          fetchTournaments()
        ])

        this.matches = matches
        this.teams = teams
        this.tournaments = tournaments
        this.error = null
      } catch (err) {
        console.error('加载赛程数据失败:', err)
        this.error = '加载赛程数据失败，请稍后再试'
      } finally {
        this.loading = false
      }
    }
  }
})