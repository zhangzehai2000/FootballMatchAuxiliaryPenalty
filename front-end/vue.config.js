// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true,
//   lintOnSave: false
// })



// module.exports 返回的是模块对象本身，返回的是一个类
module.exports = {
  devServer: {
  	// devServer.disableHostCheck配置项用于配置是否关闭用于 DNS 重绑定的 HTTP 请求的 HOST 检查
    //disableHostCheck: false,
    host: "0.0.0.0",
    port: 8091,
    // 是否配置https
    https: false,
    // hotOnly: false 如果编译报错，你再改成正确的，重新编译，浏览器会刷新
    //hotOnly: false,
    // 代理
    proxy: null
  },
  pages: {
    index: {
      // page 的入口
      entry: 'src/main.js',
    },
  },
  // 关闭语法检查
  lintOnSave: false,
  // 配置build
  publicPath: "./",
  /* # # 输出文件目录--默认dist */
  outputDir: "dist",
  /* # # 放置生成的静态资源 (js、css、img、fonts) 的 (相对于 outputDir 的) 目录。*/
  assetsDir: "static",
  /* # # 指定生成的 index.html 的输出路径 (相对于 outputDir)。也可以是一个绝对路径。*/
  indexPath: "index.html",
  // 打包提示文件体积过大导致，进行配置
  configureWebpack: (config) => {
    if (process.env.NODE_ENV === 'production') {// 为生产环境修改配置...
      config.mode = 'production';
      config["performance"] = {//打包文件大小配置
        "maxEntrypointSize": 10000000,
        "maxAssetSize": 30000000
      }
    }
  }
}

