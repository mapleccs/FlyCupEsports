import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import matchService from '@/services/matchService'

// 在文件顶部添加
const isDevelopment = process.env.NODE_ENV === 'development'

// 模拟英雄数据
const mockHeroes = [
  { id: 1, name: '盖伦', role: '战士', avatar: 'garen.png' },
  { id: 2, name: '亚索', role: '刺客', avatar: 'yasuo.png' },
  { id: 3, name: '拉克丝', role: '法师', avatar: 'lux.png' },
  { id: 4, name: '艾希', role: '射手', avatar: 'ashe.png' },
  { id: 5, name: '布里茨', role: '坦克', avatar: 'blitzcrank.png' },
  { id: 6, name: '李青', role: '战士', avatar: 'leesin.png' },
  { id: 7, name: '阿狸', role: '法师', avatar: 'ahri.png' },
  { id: 8, name: '德莱文', role: '射手', avatar: 'draven.png' },
  { id: 9, name: '锤石', role: '辅助', avatar: 'thresh.png' },
  { id: 10, name: '剑圣', role: '刺客', avatar: 'zed.png' },
  { id: 11, name: '蔚', role: '刺客', avatar: 'zed.png' },
  { id: 12, name: '霞', role: '刺客', avatar: 'zed.png' },
  { id: 13, name: '轮子妈', role: '刺客', avatar: 'zed.png' },
  { id: 14, name: '维鲁斯', role: '刺客', avatar: 'zed.png' },
  { id: 15, name: '露露', role: '刺客', avatar: 'zed.png' },
  { id: 16, name: '大嘴', role: '刺客', avatar: 'zed.png' },
  { id: 17, name: '龙王', role: '刺客', avatar: 'zed.png' },
  { id: 18, name: '小火龙', role: '刺客', avatar: 'zed.png' },
  { id: 19, name: '赛纳', role: '刺客', avatar: 'zed.png' },
  { id: 20, name: '卢锡安', role: '刺客', avatar: 'zed.png' },
]

// 模拟队伍数据
const mockTeams = [
  {
    id: 1,
    name: '无畏战队',
    logo: 'team1.png',
    captain: { id: 101, name: '张队长', avatar: 'captain1.png' },
    players: [
      { id: 102, name: '王选手', position: '上单' },
      { id: 103, name: '李选手', position: '打野' },
      { id: 104, name: '赵选手', position: '中单' },
      { id: 105, name: '钱选手', position: 'ADC' },
      { id: 106, name: '孙选手', position: '辅助' }
    ]
  },
  {
    id: 2,
    name: '荣耀战队',
    logo: 'team2.png',
    captain: { id: 201, name: '刘队长', avatar: 'captain2.png' },
    players: [
      { id: 202, name: '周选手', position: '上单' },
      { id: 203, name: '吴选手', position: '打野' },
      { id: 204, name: '郑选手', position: '中单' },
      { id: 205, name: '王选手', position: 'ADC' },
      { id: 206, name: '冯选手', position: '辅助' }
    ]
  }
]

export const useMatchStore = defineStore('match', () => {
  const matchData = ref(null)
  const checkInStatus = ref({})
  const isBPEnabled = ref(false)
  const currentPhase = ref('checkin') // checkin, banning, picking, completed
  const bans = ref({ team1: [], team2: [] })
  const picks = ref({ team1: [], team2: [] })
  const availableHeroes = ref([...mockHeroes])

  // 获取比赛详情（模拟数据）
  const fetchMatch = async (matchId) => {
    // 模拟API请求延迟
    await new Promise(resolve => setTimeout(resolve, 500))

    // 生成模拟比赛数据
    matchData.value = {
      id: matchId,
      name: `英雄联盟夏季赛 - ${matchId}号比赛`,
      date: new Date().toLocaleDateString(),
      time: '19:00',
      status: 'scheduled',
      teams: mockTeams
    }

    // 初始化签到状态
    checkInStatus.value = {
      1: false, // 队伍1未签到
      2: false  // 队伍2未签到
    }

    isBPEnabled.value = false
    currentPhase.value = 'checkin'
    return matchData.value
  }

  // 处理签到（模拟）
  const handleCheckIn = async (teamId) => {
    // 模拟API请求延迟
    await new Promise(resolve => setTimeout(resolve, 300))

    // 更新签到状态
    checkInStatus.value[teamId] = true

    // 检查是否所有队伍都已签到
    const allChecked = Object.values(checkInStatus.value).every(status => status)

    if (allChecked) {
      // 所有队伍已签到，启用BP
      await enableBP()
    }
  }

  // 启用BP功能（模拟）
  const enableBP = async () => {
    await new Promise(resolve => setTimeout(resolve, 500))
    isBPEnabled.value = true
    currentPhase.value = 'banning'
  }

  // 处理BP操作（模拟）
  const handleBPSelection = (heroId, actionType) => {
    const hero = availableHeroes.value.find(h => h.id === heroId)
    if (!hero) return

    // 从可用英雄中移除
    availableHeroes.value = availableHeroes.value.filter(h => h.id !== heroId)

    // 添加到对应队伍
    const currentTeam = getCurrentTurnTeam()

    if (actionType === 'ban') {
      bans.value[currentTeam].push(hero)
    } else {
      picks.value[currentTeam].push(hero)
    }

    // 检查是否完成BP
    checkBPCompletion()
  }

  // 获取当前操作的队伍
  const getCurrentTurnTeam = () => {
    // 简化逻辑：轮流操作
    const totalActions = [
      ...bans.value.team1,
      ...bans.value.team2,
      ...picks.value.team1,
      ...picks.value.team2
    ].length

    return totalActions % 2 === 0 ? 'team1' : 'team2'
  }

  // 检查BP是否完成
  const checkBPCompletion = () => {
    // 每队3个ban位，5个pick位
    if (bans.value.team1.length + bans.value.team2.length === 6 &&
        picks.value.team1.length + picks.value.team2.length === 10) {
      currentPhase.value = 'completed'
    } else if (bans.value.team1.length + bans.value.team2.length === 6) {
      currentPhase.value = 'picking'
    }
  }

  // 重置BP（仅用于开发测试）
  const resetBP = () => {
    bans.value = { team1: [], team2: [] }
    picks.value = { team1: [], team2: [] }
    availableHeroes.value = [...mockHeroes]
    currentPhase.value = 'banning'
  }

  // 计算属性
  const teams = computed(() => matchData.value?.teams || [])
  const isAllCheckedIn = computed(() => isBPEnabled.value)
  const currentTeamTurn = computed(() => {
    const teamId = getCurrentTurnTeam() === 'team1' ? 1 : 2
    return teams.value.find(t => t.id === teamId)
  })

  return {
    matchData,
    checkInStatus,
    isBPEnabled,
    teams,
    isAllCheckedIn,
    bans,
    picks,
    availableHeroes,
    currentPhase,
    currentTeamTurn,
    fetchMatch,
    handleCheckIn,
    handleBPSelection,
    resetBP
  }
})