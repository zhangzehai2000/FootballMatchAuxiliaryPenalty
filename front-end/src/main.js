import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css'
import VueRouter from "vue-router";
import router from "./view/router/Router.js"  //引用Router.js声明为router
import axios from 'axios'
import '../src/view/config/axios'
import qs from 'qs'
import Cookies from 'js-cookie'

Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(VueRouter)

Vue.prototype.$axios = axios  //全局注册，使用方法为：this.$axios
Vue.prototype.qs = qs   //全局注册，使用方法为：this.qs
Vue.prototype.$cookies = Cookies;

new Vue({
  router: router, //将router放在Vue组件容器，进行全局生效
  render: h => h(App),
}).$mount('#app')
