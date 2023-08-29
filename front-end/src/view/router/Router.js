import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

// 关键字: let 和 const。
// let 声明的变量只在 let 命令所在的代码块内有效。
// const 声明一个只读的常量，一旦声明，常量的值就不能改变。
// new的作用是通过构造函数来创建一个实例对象。

// 创建router 对路由进行管理，它是由构造函数 new vueRouter() 创建，接受routes 参数
const router = new VueRouter({
  routes: [
    {
      path: '/login',  // 路径
      // component是指组件  import引用login.vue地址
      component: ()=>import('../web/login/Login.vue')
    },
    {
      path: '/home',  // 路径
      redirect: '/home/penalize',
      component: ()=>import('../web/home/Home.vue'),
      // children子路由，子路由是不需要待/的，路径是/home/user_info
      children: [
        {
          path: 'user_info',
          component: ()=>import('../web/user/UserInfo.vue')
        },
        {
          path: '/home/penalize',
          name: 'penalize',
          component: () =>import("@/view/web/Framework/Penalize")
        },
        {
          path: '/home/slideTackle',
          name: 'slideTackle',
          component: () =>import("@/view/web/Framework/SlideTackle")
        },
        {
          path: '/home/premierLeague',
          name: 'premierLeague',
          component: () =>import("@/view/web/Framework/PremierLeague")
        },
      ]
    },

  ]
})

// import Cookies from 'js-cookie'
//
// router.beforeEach((to, form, next) => {
//   // 进入的路径是根目录
//   if (to.path == '/login') {
//     // 那么就跳转到下一个路径
//     next()
//   } else {
//     // 如果不是根目录，获取token然后进行判断
//     const token = Cookies.get('token')
//     console.log("1")
//     if (!token) {
//       // if过假的就跳转到根目录
//       next('/login')
//     } else {
//       // 否则正常跳转到下一个目录
//       next()
//     }
//   }
// })


export default router
