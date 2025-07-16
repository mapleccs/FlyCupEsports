
## GET /api/v1/user
### 响应参数
| 字段名        | 类型             | 描述  |
|------------|----------------|-----|
| id         | string         | 编号  |
| user_name  | string         | 密码  |
| photo_path | string \| null | 用户名 |

**示例**
```json
[
    {
        "id": 1,
        "user_name": "卷卷",
        "photo_path": null
    },
    {
        "id": 2,
        "user_name": "test",
        "photo_path": "test"
    }
]
```

### 说明：
photo_path 如果没有，结果为null。

## POST /api/v1/user/register
### 请求参数
| 字段名         | 类型     | 是否必填 | 描述         |
|-------------|--------|------|------------|
| user\_name  | string | 是    | 用户名        |
| password    | string | 是    | 密码         |
| photo\_path | string | 否    | 用户头像路径（可选） |
| role        | string | 否    | 角色名（可选）    |
**示例**
```json
{
    "user_name":"T5",
    "password":"123456",
    "photo_path":"",
    "role":"User"
}
```

### 响应参数
| 字段名     | 类型              | 描述                 |
| ------- | --------------- | ------------------ |
| success | boolean         | 操作是否成功             |
| userId  | integer \| null | 创建的用户ID，失败时可能为null |
| message | string          | 提示信息               |

**示例**
```json
{
    "success": true,
    "user_id": 4,
    "message": "User created successfully."
}
```

### 说明：
photo_path 是可选字段，可以不传。
role 默认为User
当创建失败时，success 为 false，userId 可能为 null，并携带错误提示信息。
