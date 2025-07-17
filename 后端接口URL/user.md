
## GET /api/v1/user
### 响应参数
| 字段名            | 类型             | 描述   |
|----------------|----------------|------|
| id             | string         | 编号   |
| username       | string         | 用户名  |
| photo_path     | string \| null | 头像路径 |
| user_role_id   | integer        | 角色编号 |
| user_role_name | string         | 角色名称 |

**示例**
```json
[
    {
        "id": 1,
        "username": "admin",
        "photo_path": null,
        "user_role_id": 1,
        "user_role_name": "admin"
    }
]
```

### 说明：
photo_path 如果没有，结果为null。

## POST /api/v1/user/register
### 请求参数
| 字段名         | 类型     | 是否必填 | 描述         |
|-------------|--------|------|------------|
| username    | string | 是    | 用户名        |
| password    | string | 是    | 密码         |
| photo\_path | string | 否    | 用户头像路径（可选） |
| role        | string | 是    | 角色名        |
**示例**
```json
{
    "username":"admin",
    "password":"123456",
    "photo_path":"",
    "role":"user"
}
```
```json
{
    "username":"admin",
    "password":"123456",
    "role":"user"
}
```

### 响应参数
| 字段名     | 类型              | 描述                 |
|---------|-----------------|--------------------|
| success | boolean         | 操作是否成功             |
| userId  | integer \| null | 创建的用户ID，失败时可能为null |
| message | string          | 提示信息               |

**示例**
```json
{
    "success": true,
    "user_id": 1,
    "message": "User created successfully."
}
```

### 说明：
photo_path 是可选字段，可以不传。
role 默认为User
当创建失败时，success 为 false，userId 可能为 null，并携带错误提示信息。


## POST /api/v1/user/login
### 请求参数
| 字段名       | 类型     | 是否必填 | 描述         |
|-----------|--------|------|------------|
| username  | string | 是    | 用户名        |
| password  | string | 是    | 密码         |
**示例**
```json
{
    "username":"admin",
    "password":"123456"
}
```

### 响应参数
| 字段名            | 类型              | 描述                 |
|----------------|-----------------|--------------------|
| success        | boolean         | 操作是否成功             |
| userId         | integer \| null | 创建的用户ID，失败时可能为null |
| user_role_id   | integer \| null | 角色编号，失败时可能为null    |
| user_role_name | string \| null  | 角色命名，失败时可能为null    |
| message        | string          | 提示信息               |

**示例**
```json
{
    "success": true,
    "user_id": 1,
    "user_role_id": 2,
    "user_role_name": "User",
    "message": "Login successfully."
}
```
