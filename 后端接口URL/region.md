## GET /api/v1/region

### 响应参数

| 字段名                    | 类型             | 描述     |
|------------------------|----------------|--------|
| season_name            | string         | 赛季名    |
| name                   | string         | 赛区名    |
| username               | string \| null | 负责人名   |
| logo                   | string         | 路径     |
| max_team_limit         | integer        | 最大队伍上限 |
| end_register_date      | string         | 注册结束日期 |
| start_competition_date | string         | 开始比赛日期 |
| end_competition_date   | string         | 比赛结束如期 |

**示例**

```json
[
  {
    "season_name": "第一赛季",
    "name": "FLY",
    "username": "admin",
    "logo": "",
    "max_team_limit": 16,
    "end_register_date": "2025-07-20",
    "start_competition_date": "2025-07-21",
    "end_competition_date": "2025-09-20"
  }
]
```

### 说明：

photo_path 如果没有，结果为null。
