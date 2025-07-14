// 赛区数据
export const regions = [
  {
    id: 'fly',
    name: 'FLY赛区',
    icon: 'el-icon-trophy',
    description: '面向高端玩家的专业级赛事',
    teams: 32,
    players: 320,
    fee: 50
  },
]

// 支付方式
export const paymentMethods = [
  { id: 'wechat', name: '微信支付', icon: 'el-icon-chat-line-round' },
  { id: 'alipay', name: '支付宝', icon: 'el-icon-money' },
  { id: 'bank', name: '银行卡', icon: 'el-icon-credit-card' }
]

// 位置选项
export const positions = [
  { value: 'top', label: '上单' },
  { value: 'jungle', label: '打野' },
  { value: 'mid', label: '中单' },
  { value: 'adc', label: 'ADC' },
  { value: 'support', label: '辅助' }
]

// 段位选项
export const ranks = [
    { value: 'challenger', label: '王者' },
    { value: 'grandmaster', label: '宗师' },
    { value: 'master', label: '大师' },
    { value: 'diamond', label: '钻石' },
    { value: 'emerald', label: '翡翠' },
    { value: 'platinum', label: '铂金' },
    { value: 'gold', label: '黄金' },
    { value: 'silver', label: '白银' },
    { value: 'bronze', label: '青铜' },
    { value: 'iron', label: '黑铁' },
]