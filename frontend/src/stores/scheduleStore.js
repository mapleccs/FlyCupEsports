import { defineStore } from 'pinia'

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
        // 模拟延迟
        await new Promise(resolve => setTimeout(resolve, 800))

        // 模拟数据
        this.teams = [
          { id: 1, name: 'EDG电子竞技俱乐部', abbr: 'EDG', logo: 'https://zhihuiss2024.oss-cn-nanjing.aliyuncs.com/img/202507172213289.png', region: 'LPL' },
          { id: 2, name: 'RNG电子竞技俱乐部', abbr: 'RNG', logo: 'https://zhihuiss2024.oss-cn-nanjing.aliyuncs.com/img/202507172213289.png', region: 'LPL' },
          { id: 3, name: 'IG电子竞技俱乐部', abbr: 'IG', logo: 'https://zhihuiss2024.oss-cn-nanjing.aliyuncs.com/img/202507172213289.png', region: 'LPL' },
          { id: 4, name: 'FPX电子竞技俱乐部', abbr: 'FPX', logo: 'https://zhihuiss2024.oss-cn-nanjing.aliyuncs.com/img/202507172213289.png', region: 'LPL' },
          { id: 5, name: 'TES电子竞技俱乐部', abbr: 'TES', logo: 'https://zhihuiss2024.oss-cn-nanjing.aliyuncs.com/img/202507172213289.png', region: 'LPL' },
          { id: 6, name: 'JDG京东电子竞技俱乐部', abbr: 'JDG', logo: 'https://zhihuiss2024.oss-cn-nanjing.aliyuncs.com/img/202507172213289.png', region: 'LPL' },
          { id: 7, name: 'LNG电子竞技俱乐部', abbr: 'LNG', logo: 'https://zhihuiss2024.oss-cn-nanjing.aliyuncs.com/img/202507172213289.png', region: 'LPL' },
          { id: 8, name: 'WE电子竞技俱乐部', abbr: 'WE', logo: 'https://zhihuiss2024.oss-cn-nanjing.aliyuncs.com/img/202507172213289.png', region: 'LPL' },
          { id: 9, name: 'T1', abbr: 'T1', logo: 'https://zhihuiss2024.oss-cn-nanjing.aliyuncs.com/img/202507172213289.png', region: 'LCK' },
          { id: 10, name: 'Gen.G', abbr: 'GEN', logo: 'https://zhihuiss2024.oss-cn-nanjing.aliyuncs.com/img/202507172213289.png', region: 'LCK' },
          { id: 11, name: 'DK', abbr: 'DK', logo: 'https://zhihuiss2024.oss-cn-nanjing.aliyuncs.com/img/202507172213289.png', region: 'LCK' },
          { id: 12, name: 'G2 Esports', abbr: 'G2', logo: 'https://zhihuiss2024.oss-cn-nanjing.aliyuncs.com/img/202507172213289.png', region: 'LEC' },
          { id: 13, name: 'Fnatic', abbr: 'FNC', logo: 'https://zhihuiss2024.oss-cn-nanjing.aliyuncs.com/img/202507172213289.png', region: 'LEC' },
          { id: 14, name: 'Cloud9', abbr: 'C9', logo: 'https://zhihuiss2024.oss-cn-nanjing.aliyuncs.com/img/202507172213289.png', region: 'LCS' },
          { id: 15, name: 'Team Liquid', abbr: 'TL', logo: 'https://zhihuiss2024.oss-cn-nanjing.aliyuncs.com/img/202507172213289.png', region: 'LCS' }
        ]

        this.tournaments = [
          { id: 1, name: 'LPL春季赛', logo: '/logos/lpl.png', season: '2023春季' },
          { id: 2, name: 'LPL夏季赛', logo: '/logos/lpl.png', season: '2023夏季' },
          { id: 3, name: '德玛西亚杯', logo: '/logos/demacia.png', season: '2023' },
          { id: 4, name: 'MSI季中冠军赛', logo: '/logos/msi.png', season: '2023' },
          { id: 5, name: '英雄联盟全球总决赛', logo: '/logos/worlds.png', season: '2023' }
        ]

        this.matches = [
          // 已结束的比赛
          {
            id: 1,
            date: '2025-07-20',
            time: '17:00',
            tournament: this.tournaments[1],
            stage: '常规赛',
            teamA: this.teams[0],
            teamB: this.teams[1],
            scoreA: 2,
            scoreB: 1,
            status: 'completed',
            replayUrl: 'https://www.bilibili.com/video/BV1dP4y1p7Jz',
            stats: {
              duration: '32:15',
              killsA: 24,
              killsB: 18,
              towersA: 9,
              towersB: 4,
              dragonsA: 3,
              dragonsB: 2,
              baronsA: 1,
              baronsB: 0
            }
          },
          {
            id: 2,
            date: '2025-07-20',
            time: '19:00',
            tournament: this.tournaments[1],
            stage: '常规赛',
            teamA: this.teams[2],
            teamB: this.teams[3],
            scoreA: 0,
            scoreB: 2,
            status: 'completed',
            replayUrl: 'https://www.bilibili.com/video/BV1dP4y1p7Jz',
            stats: {
              duration: '28:42',
              killsA: 8,
              killsB: 22,
              towersA: 2,
              towersB: 9,
              dragonsA: 1,
              dragonsB: 3,
              baronsA: 0,
              baronsB: 1
            }
          },
          // 未开始的比赛
          {
            id: 3,
            date: '2025-07-21',
            time: '17:00',
            tournament: this.tournaments[1],
            stage: '常规赛',
            teamA: this.teams[4],
            teamB: this.teams[5],
            status: 'upcoming'
          },
          {
            id: 4,
            date: '2025-07-21',
            time: '19:00',
            tournament: this.tournaments[1],
            stage: '常规赛',
            teamA: this.teams[6],
            teamB: this.teams[7],
            status: 'upcoming'
          },
          // 直播中的比赛
          {
            id: 5,
            date: '2025-07-22',
            time: '17:00',
            tournament: this.tournaments[1],
            stage: '常规赛',
            teamA: this.teams[0],
            teamB: this.teams[4],
            status: 'live',
            liveUrl: 'https://live.bilibili.com/25079843'
          },
          {
            id: 6,
            date: '2025-07-22',
            time: '19:00',
            tournament: this.tournaments[1],
            stage: '常规赛',
            teamA: this.teams[1],
            teamB: this.teams[5],
            status: 'upcoming'
          },
          // 其他赛事
          {
            id: 7,
            date: '2025-07-23',
            time: '15:00',
            tournament: this.tournaments[3],
            stage: '小组赛',
            teamA: this.teams[2],
            teamB: this.teams[8],
            status: 'upcoming'
          },
          {
            id: 8,
            date: '2025-07-23',
            time: '17:00',
            tournament: this.tournaments[3],
            stage: '小组赛',
            teamA: this.teams[3],
            teamB: this.teams[9],
            status: 'upcoming'
          },
          {
            id: 9,
            date: '2025-07-23',
            time: '19:00',
            tournament: this.tournaments[3],
            stage: '小组赛',
            teamA: this.teams[0],
            teamB: this.teams[11],
            status: 'upcoming'
          },
          {
            id: 10,
            date: '2025-07-24',
            time: '17:00',
            tournament: this.tournaments[1],
            stage: '常规赛',
            teamA: this.teams[6],
            teamB: this.teams[0],
            status: 'upcoming'
          },
          {
            id: 11,
            date: '2025-07-24',
            time: '19:00',
            tournament: this.tournaments[1],
            stage: '常规赛',
            teamA: this.teams[7],
            teamB: this.teams[1],
            status: 'upcoming'
          },
          {
            id: 12,
            date: '2025-07-25',
            time: '17:00',
            tournament: this.tournaments[1],
            stage: '常规赛',
            teamA: this.teams[4],
            teamB: this.teams[2],
            status: 'upcoming'
          },
          {
            id: 13,
            date: '2025-07-25',
            time: '19:00',
            tournament: this.tournaments[1],
            stage: '常规赛',
            teamA: this.teams[5],
            teamB: this.teams[3],
            status: 'upcoming'
          }
        ]

        this.error = null
      } catch (error) {
        console.error('加载赛程数据失败:', error)
        this.error = '加载赛程数据失败，请稍后再试'
      } finally {
        this.loading = false
      }
    }
  }
})