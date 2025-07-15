// 赛区数据
export const regions = [
  {
    id: 'fly',
    name: 'FLY赛区',
    icon: 'el-icon-trophy',
    description: '面向高端玩家的专业级赛事',
    teams: 32,
    players: 320,
    fee: 50000
  },
  {
    id: 'pfp',
    name: 'PFP赛区',
    icon: 'el-icon-trophy',
    description: '面向低端玩家的专业级赛事',
    teams: 16,
    players: 200,
    fee: 5
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
    { value: '王者', label: '王者' },
    { value: '宗师', label: '宗师' },
    { value: '大师', label: '大师' },
    { value: '钻石', label: '钻石' },
    { value: '翡翠', label: '翡翠' },
    { value: '铂金', label: '铂金' },
    { value: '黄金', label: '黄金' },
    { value: '白银', label: '白银' },
    { value: '青铜', label: '青铜' },
    { value: '黑铁', label: '黑铁' },
]