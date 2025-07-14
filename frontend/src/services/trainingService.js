import axios from 'axios'

// 模拟数据
const mockSessions = [
  {
    id: 1,
    team: {
      id: 1,
      name: "IG战队",
      region: "FLY",
      logo: "team1.png"
    },
    title: "寻找实力相当的战队进行BO3训练赛",
    date: "2023-10-25",
    time: "19:00",
    duration: 2.5,
    mode: "BO3训练赛",
    requirements: "战队段位钻石以上",
    description: "我们是一支钻石段位的战队，寻找实力相当的队伍进行训练赛，提升团队配合和战术执行力。",
    status: "open",
    applications: [
      {
        id: 101,
        team: {
          id: 2,
          name: "FPX战队",
          region: "FLY",
          logo: "team2.png"
        },
        message: "我们战队也是钻石段位，希望可以和你们切磋学习"
      },
      {
        id: 102,
        team: {
          id: 3,
          name: "EDG战队",
          region: "PFP",
          logo: "team3.png"
        },
        message: "我们刚刚晋级钻石，希望和强队学习"
      }
    ]
  },
  {
    id: 2,
    team: {
      id: 2,
      name: "IG战队",
      region: "FLY",
      logo: "team2.png"
    },
    title: "自定义模式练习新阵容",
    date: "2023-10-26",
    time: "20:30",
    duration: 2,
    mode: "自定义模式",
    requirements: "",
    description: "练习新赛季的阵容搭配和战术体系，欢迎任何段位的战队参加",
    status: "open",
    applications: []
  },
  {
    id: 3,
    team: {
      id: 3,
      name: "EDG战队",
      region: "PFP",
      logo: "team3.png"
    },
    title: "周末BO5训练赛",
    date: "2023-10-28",
    time: "14:00",
    duration: 3,
    mode: "BO5训练赛",
    requirements: "战队段位铂金以上",
    description: "周末长时间训练赛，寻找有耐心的战队一起提升",
    status: "accepted",
    applications: []
  }
]

// 获取训练赛预约列表
export async function getTrainingSessions(type = 'available') {
  try {
    // 实际开发中，这里应该是从后端API获取数据
    // 例如: const response = await axios.get(`/api/training-sessions?type=${type}`)

    // 模拟API调用
    return new Promise(resolve => {
      setTimeout(() => {
        // 根据类型过滤数据
        let result = [...mockSessions]

        if (type === 'available') {
          result = result.filter(s => s.status === 'open')
        } else if (type === 'my-published') {
          // 假设当前用户ID为1（雷霆战队）
          result = result.filter(s => s.team.id === 1)
        }

        resolve(result)
      }, 500)
    })
  } catch (error) {
    console.error('获取训练赛数据失败:', error)
    return []
  }
}

// 创建训练赛预约
export async function createTrainingSession(sessionData) {
  try {
    // 实际开发中：await axios.post('/api/training-sessions', sessionData)

    // 模拟创建
    return new Promise(resolve => {
      setTimeout(() => {
        const newSession = {
          id: Math.max(...mockSessions.map(s => s.id)) + 1,
          team: {
            id: 1,
            name: "IG战队",
            region: "FLY",
            logo: "team1.png"
          },
          ...sessionData,
          status: "open",
          applications: []
        }
        mockSessions.unshift(newSession)
        resolve(newSession)
      }, 500)
    })
  } catch (error) {
    console.error('创建训练赛失败:', error)
    throw error
  }
}

// 更新训练赛预约
export async function updateTrainingSession(sessionData) {
  try {
    // 实际开发中：await axios.put(`/api/training-sessions/${sessionData.id}`, sessionData)

    // 模拟更新
    return new Promise(resolve => {
      setTimeout(() => {
        const index = mockSessions.findIndex(s => s.id === sessionData.id)
        if (index !== -1) {
          mockSessions[index] = { ...mockSessions[index], ...sessionData }
        }
        resolve()
      }, 500)
    })
  } catch (error) {
    console.error('更新训练赛失败:', error)
    throw error
  }
}

// 申请训练赛预约
export async function applyForTrainingSession(application) {
  try {
    // 实际开发中：await axios.post('/api/training-applications', application)

    // 模拟申请
    return new Promise(resolve => {
      setTimeout(() => {
        const session = mockSessions.find(s => s.id === application.sessionId)
        if (session) {
          // 假设当前用户ID为2（风暴战队）
          const applyingTeam = {
            id: 2,
            name: "FPX战队",
            region: "FLY",
            logo: "team2.png"
          }

          const newApplication = {
            id: Math.max(0, ...session.applications.map(a => a.id)) + 1,
            team: applyingTeam,
            message: application.message
          }

          session.applications.push(newApplication)
        }
        resolve()
      }, 500)
    })
  } catch (error) {
    console.error('申请训练赛失败:', error)
    throw error
  }
}

// 获取我的申请
export async function getMyApplications() {
  try {
    // 实际开发中：await axios.get('/api/training-applications/me')

    // 模拟数据 - 假设当前用户ID为2（风暴战队）
    return new Promise(resolve => {
      setTimeout(() => {
        const appliedSessions = mockSessions
          .filter(s => s.applications.some(app => app.team.id === 2))
          .map(session => ({
            ...session,
            status: 'pending' // 申请状态为待处理
          }))

        resolve(appliedSessions)
      }, 500)
    })
  } catch (error) {
    console.error('获取申请列表失败:', error)
    return []
  }
}

// 取消训练赛预约
export async function cancelTrainingSession(sessionId) {
  try {
    // 实际开发中：await axios.delete(`/api/training-sessions/${sessionId}`)

    // 模拟取消
    return new Promise(resolve => {
      setTimeout(() => {
        const index = mockSessions.findIndex(s => s.id === sessionId)
        if (index !== -1) {
          mockSessions[index].status = 'cancelled'
        }
        resolve()
      }, 500)
    })
  } catch (error) {
    console.error('取消训练赛失败:', error)
    throw error
  }
}

// 取消申请
export async function cancelApplication(applicationId) {
  try {
    // 实际开发中：await axios.delete(`/api/training-applications/${applicationId}`)

    // 模拟取消申请
    return new Promise(resolve => {
      setTimeout(() => {
        for (const session of mockSessions) {
          const appIndex = session.applications.findIndex(a => a.id === applicationId)
          if (appIndex !== -1) {
            session.applications.splice(appIndex, 1)
            break
          }
        }
        resolve()
      }, 500)
    })
  } catch (error) {
    console.error('取消申请失败:', error)
    throw error
  }
}

// 接受申请
export async function acceptApplication(applicationId) {
  try {
    // 实际开发中：await axios.post(`/api/training-applications/${applicationId}/accept`)

    // 模拟接受申请
    return new Promise(resolve => {
      setTimeout(() => {
        for (const session of mockSessions) {
          const application = session.applications.find(a => a.id === applicationId)
          if (application) {
            session.status = 'accepted'
            // 实际应用中这里应该只保留被接受的申请，但为演示简单保留所有
            break
          }
        }
        resolve()
      }, 500)
    })
  } catch (error) {
    console.error('接受申请失败:', error)
    throw error
  }
}

// 拒绝申请
export async function rejectApplication(applicationId) {
  try {
    // 实际开发中：await axios.post(`/api/training-applications/${applicationId}/reject`)

    // 模拟拒绝申请
    return new Promise(resolve => {
      setTimeout(() => {
        for (const session of mockSessions) {
          const appIndex = session.applications.findIndex(a => a.id === applicationId)
          if (appIndex !== -1) {
            session.applications[appIndex].status = 'rejected'
            break
          }
        }
        resolve()
      }, 500)
    })
  } catch (error) {
    console.error('拒绝申请失败:', error)
    throw error
  }
}

// 获取训练赛历史
export async function getTrainingHistory() {
  try {
    // 实际开发中：await axios.get('/api/training-sessions/history')

    // 模拟历史数据
    return new Promise(resolve => {
      setTimeout(() => {
        const history = [
          ...mockSessions.filter(s => s.status !== 'open'),
          {
            id: 4,
            team: {
              id: 1,
              name: "IG战队",
              region: "FLY",
              logo: "team1.png"
            },
            title: "上周末BO3训练赛",
            date: "2023-10-15",
            time: "15:00",
            duration: 2.5,
            mode: "BO3训练赛",
            status: "completed",
            applications: []
          },
          {
            id: 5,
            team: {
              id: 3,
              name: "FPX战队",
              region: "FLY",
              logo: "team3.png"
            },
            title: "上周自定义训练",
            date: "2023-10-12",
            time: "20:00",
            duration: 2,
            mode: "自定义模式",
            status: "completed",
            applications: []
          }
        ]
        resolve(history)
      }, 500)
    })
  } catch (error) {
    console.error('获取历史记录失败:', error)
    return []
  }
}