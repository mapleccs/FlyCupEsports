## User接口


### GET /api/v1/user
**Response**
```json
[
    {
        "UserName": "卷卷",
        "Password": "123456",
        "Id": 1,
        "UserPhoto": null
    },
    {
        "UserName": "test",
        "Password": "123456",
        "Id": 2,
        "UserPhoto": "test"
    }
]
```

### POST /api/v1/user/register
**Request**
```json
{
    "user_name":"test",
    "password":"123456",
    "photo_path":"test"
}
```
**Response**
```json
{
    "success": true,
    "userId": 2,
    "message": "User created successfully."
}
```


