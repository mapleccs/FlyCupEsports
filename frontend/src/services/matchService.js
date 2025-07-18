// 使用模拟数据，实际项目中替换为真实API调用
export default {
  getMatchDetails(matchId) {
    // 实际实现: return api.get(`/matches/${matchId}`)
    return Promise.resolve({ data: {} })
  },

  checkIn(matchId, teamId) {
    // 实际实现: return api.post(`/matches/${matchId}/checkin`, { teamId })
    return Promise.resolve({ updatedStatus: {} })
  },

  enableBP(matchId) {
    // 实际实现: return api.post(`/matches/${matchId}/enable-bp`)
    return Promise.resolve({})
  },

  submitBansPicks(matchId, selections) {
    // 实际实现: return api.post(`/matches/${matchId}/bp`, selections)
    return Promise.resolve({})
  }
}