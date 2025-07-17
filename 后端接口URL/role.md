
## GET /api/v1/role
### 响应参数
| 字段名    | 类型             | 描述  |
|--------|----------------|-----|
| id     | string         | 编号  |
| name   | string         | 角色名 |
| remark | string \| null | 备注  |

**示例**
```json
[
    {
        "id": 1,
        "name": "Admin",
        "remark": "管理员"
    },
    {
        "id": 2,
        "name": "User",
        "remark": "用户、游客"
    },
    {
        "id": 3,
        "name": "Player",
        "remark": "选手"
    }
]
```