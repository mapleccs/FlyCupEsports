## POST /api/v1/player/register

### 请求参数

| 字段名                | 类型      | 是否必填 | 描述   |
|--------------------|---------|------|------|
| personal_name      | string  | 是    | 用户名  |
| gameId             | string  | 是    | 游戏名  |
| main_position      | string  | 否    | 主位置  |
| secondary_position | string  | 是    | 副位置  |
| highest_rank       | string  | 是    | 最高段位 |
| current_rank       | string  | 是    | 当前段位 |
| QQ                 | string  | 是    | QQ号  |
| contact            | string  | 否    | 联系人  |
| region             | integer | 是    | 地区   |
| payment_method     | string  | 是    | 支付方式 |

**示例**

```json
{
    "personal_name": "影流之主",
    "gameId": "ShadowBlade#1234",
    "main_position": "mid",
    "secondary_position": "jungle",
    "highest_rank": "王者",
    "current_rank": "大师",
    "QQ": "123456789",
    "contact": "13800138000",
    "region": 1,
    "payment_method": "微信支付"
}
```

### 响应参数

| 字段名          | 类型             | 描述                 |
|--------------|----------------|--------------------|
| success      | boolean        | 操作是否成功             |
| player_token | string \| null | 创建的选手ID，失败时可能为null |
| message      | string         | 提示信息               |

**示例**

```json
{
    "success": true,
    "player_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF5ZXJfaWQiOjcsImV4cCI6MTc1MjgxNDgwMX0.ym-00emd1IjM-jOqZQAA3A5-6yfH6u8wXBv99vFIfZ8",
    "message": "User created successfully."
}
```
