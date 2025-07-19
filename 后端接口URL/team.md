## POST /api/v1/team/register

### 请求参数

| 字段名       | 类型      | 是否必填 | 描述     |
|-----------|---------|------|--------|
| name      | string  | 是    | 战队名    |
| shortname | string  | 是    | 缩写     |
| logo      | string  | 否    | 队伍logo |
| slogan    | string  | 是    | 口号     |
| region_id | integer | 是    | 赛区     |

**示例**
bearer token:user_id
```json
{
    "name":"test",
    "shortname":"t",
    "logo":"textpath",
    "slogan":"slog",
    "region_id":1
}
```

### 响应参数

| 字段名        | 类型             | 描述                    |
|------------|----------------|-----------------------|
| success    | boolean        | 操作是否成功                |
| team_token | string \| null | 创建的队伍token，失败时可能为null |
| message    | string         | 提示信息                  |

**示例**

```json
{
    "success": true,
    "team_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZWFtX2lkIjoxLCJleHAiOjE3NTI4OTE5MjN9.eDEJa4AeLINfXZI4ZjILhiTsQ4bid0_YoaVRio2hWbk",
    "message": "team created successfully."
}
```

```json
{
    "success": false,
    "team_token": null,
    "message": "同一个大区中不能有相同名称和简称的队伍"
}
```

