<template>
  <el-container className="home_container">

    <!-- header -->
    <el-header style="height:50px">
      <!-- 局部方法复用 -->
      <Header/>
    </el-header>

    <!-- 左侧导航栏 -->
    <el-container>
      <!-- 局部方法复用 -->
      <Navigation/>

      <el-container>
        <!-- 主体内容 -->
        <el-main>
          <!-- 路由统一跳转 -->
          <router-view></router-view>
        </el-main>
      </el-container>

    </el-container>
  </el-container>
</template>
<script>
// 引入Header、Navigation组件
import Header from "../Framework/Header.vue";
import Navigation from "../Framework/Navigation.vue";

export default {
  // 给组件命名为Home
  name: "home",
  // 组件 (Component) 是 Vue.js 最强大的功能之一。组件可以扩展 HTML 元素，封装可重用的代码。在这里我们复用Header、Navigation组件
  components: {
    // 复用Header组件
    Header,
    // 复用Navigation组件
    Navigation
  },
  data() {
    return {};
  },
};
</script>

<style scoped="scoped">
/* 当一个style标签拥有scoped属性时候，它的css样式只能用于当前的Vue组件，可以使组件的样式不相互污染 */
.home_container {
  width: 100%;
  height: 100%;
}

.Retract {
  color: rgba(255, 255, 255, 0.952);
}

.el-main {
  background: rgb(255, 255, 255);
}

.el-header {
  padding: 0px;
}
</style>
