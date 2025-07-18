// frontend/vue.config.js

const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '/api': { // 匹配所有以 '/api' 开头的请求
        target: 'http://127.0.0.1:8000', // 目标后端服务器地址
        changeOrigin: true, // 改变请求源, 这是必须的
        ws: true, // 如果您需要websocket, 也一并配置
        // 可选：重写路径。如果后端接口本身没有/api前缀，则需要重写
        // pathRewrite: {
        //   '^/api': ''
        // }
      }
    }
  }
});