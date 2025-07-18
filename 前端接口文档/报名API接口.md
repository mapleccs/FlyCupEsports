# 前端返回接口

### 1.选手报名接口

- **URL**: `/api/signup/player`

- **Method**: POST

- **Headers**:

  - `Authorization: Bearer <token>`

- **Request Body**:

  ```json
  {
    "personal_name": "选手昵称",
    "gameId": "游戏ID",
    "main_position": "top|jungle|mid|adc|support",
    "secondary_position": "top|jungle|mid|adc|support",
    "highest_rank": "段位值",
    "current_rank": "段位值",
    "QQ": "QQ号",
    "contact": "联系方式",
    "region": "赛区ID"
  }
  ```

### 2. 战队报名接口

- **URL**: `/api/signup/team`

- **Method**: POST

- **Headers**:

  - `Authorization: Bearer <token>`

- **Request Body**:

  ```json
  {
    "name": "战队名称",
    "shortName": "战队简称",
    "logo": "logo URL",
    "slogan": "战队口号",
    "region": "赛区ID"
  }
  ```

### 3. 微信支付订单创建接口

- **URL**: `/api/signup/payment/wechat`

- **Method**: POST

- **Headers**:

  - `Authorization: Bearer <token>`

- **Request Body**:

  ```json
  {
    "orderId": "报名记录ID",
    "amount": 金额,
    "description": "订单描述",
    "openid": "用户微信openid",
    "clientIp": "用户IP"
  }
  ```

### 4. 支付状态查询接口

- **URL**: `/api/signup/payment/status/:orderId`

- **Method**: GET

- **Headers**:

  - `Authorization: Bearer <token>`

- **Response**:

  ```json
  {
    "status": "success|pending|failed",
    "orderId": "订单ID",
    "amount": 金额,
    "paidAt": "支付时间"
  }
  ```

