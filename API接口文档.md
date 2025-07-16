### 选手注册

```json
POST /api/v1/players
Request Body:
{
  "personal_name": "选手昵称",
  "gameId": "游戏ID",
  "main_position": "主玩位置",
  "secondary_position": "次玩位置",
  "highest_rank": "最高段位",
  "current_rank": "当前段位",
  "QQ": "QQ号",
  "contact": "联系方式",
  "region": "赛区ID",
  "payment_method": "支付方式"
}

Response:
{
  "success": true,
  "playerId": 12345,
  "message": "选手注册成功"
}
```



### 战队注册

```json
POST /api/v1/teams
Request Body:
{
  "name": "战队名称",
  "shortName": "战队简称",
  "logo": "logo URL",
  "slogan": "战队口号",
  "region": "赛区ID",
  "payment_method": "支付方式"
}

Response:
{
  "success": true,
  "teamId": 54321,
  "message": "战队创建成功"
}
```



### 支付API

```json
{
  "item_id": "项目ID",
  "item_type": "player/team",
  "amount": 金额,
  "method": "支付方式"
}
```





### 赛区API

```json
[
  {
    "id": "fly",
    "name": "FLY赛区",
    "description": "高手云集，精英对决",
    "teams": 16,
    "players": 80
  },
  {
    "id": "fpf",
    "name": "FPF赛区",
    "description": "新秀崛起，潜力无限",
    "teams": 24,
    "players": 120
  }
]
```





### 报名费用API

```JSON
{
  "player": 10,
  "team": 50
}
```





### 用户注册

```json
POST /auth/v1/register
{
    username: 'admin', 
    password: '123456', 
    role: 'user'
}
```



用户登陆

```json
```

