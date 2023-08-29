import axios from 'axios'

// if判断生产环境和开发环境
if (process.env.NODE_ENV === 'production') {
  // if，根据.env文件中的process.env.VUE_APP_BASE_URL判断是生产环境还是测试环境
  if (process.env.VUE_APP_BASE_URL === 'build') {
    //production 生产环境
    axios.defaults.baseURL = 'http://192.168.24.145:8090/';
  } else {
    //test 测试环境
    axios.defaults.baseURL = 'http://127.0.0.1:8090/';
  }
} else {
  //serve 开发环境
  axios.defaults.baseURL = 'http://127.0.0.1:8090/';
}


import Cookies from 'js-cookie'

  //添加请求拦截器
  axios.interceptors.request.use(function (config) {
    if (Cookies.get('token')) {

      var token = 'user_name=' + Cookies.get('username') + ';' + 'token=' + Cookies.get('token')
      config.headers['Cookies'] = token

    }else{
      console.log("暂时没有cookie", Cookies.get('tokrn'))
    }

    //在发送请求之前做些什么
    return config
  },function (error) {
    //对请求错误做些什么

    return Promise.reject(error)
  });

  //添加响应拦截器
  axios.interceptors.response.use(function (response){
    console.log()

    //对响应数据做点什么
    return response
  },function (error) {
    //对响应错误做点什么
    return Promise.reject(error)
  });