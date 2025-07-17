
## GET /api/v1/position
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
        "name": "top",
        "remark": "上单"
    },
    {
        "id": 2,
        "name": "jungle",
        "remark": "打野"
    },
    {
        "id": 3,
        "name": "mid",
        "remark": "中单"
    },
    {
        "id": 4,
        "name": "adc",
        "remark": "射手"
    },
    {
        "id": 5,
        "name": "support",
        "remark": "辅助"
    }
]
```