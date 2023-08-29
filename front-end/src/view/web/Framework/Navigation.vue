<template>
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu :default-openeds="['1', '3']" :router="true">
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-menu"></i>      犯规识别  </template>
        <el-menu-item-group>
<!--          <el-menu-item :index="this.menuList.a.path">犯规识别</el-menu-item>-->
<!--          <el-menu-item index="1-2">越位识别</el-menu-item>-->
          <el-menu-item index="penalize">越位识别</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group >
          <el-menu-item index="slideTackle">铲球犯规</el-menu-item>
        </el-menu-item-group>

<!--        <el-submenu index="1-4">-->
<!--          <template slot="title">选项4</template>-->
<!--          <el-menu-item index="1-4-1">选项4-1</el-menu-item>-->
<!--        </el-submenu>-->

      </el-submenu>

      <el-submenu index="2">
        <template slot="title"><i class="el-icon-menu"></i>  球员识别  </template>

        <el-meun-item-group>
          <el-menu-item index="premierLeague">英超</el-menu-item>
        </el-meun-item-group>
<!--        <el-menu-item-group>-->
<!--          <el-menu-item index="2-1">选项1</el-menu-item>-->
<!--          <el-menu-item index="2-2">选项2</el-menu-item>-->
<!--        </el-menu-item-group>-->
<!--        <el-menu-item-group title="分组2">-->
<!--          <el-menu-item index="2-3">选项3</el-menu-item>-->
<!--        </el-menu-item-group>-->
<!--        <el-submenu index="2-4">-->
<!--          <template slot="title">选项4</template>-->
<!--          <el-menu-item index="2-4-1">选项4-1</el-menu-item>-->
<!--        </el-submenu>-->

      </el-submenu>
    </el-menu>
  </el-aside>
</template>

<script>

  export default {
    name: "Navigation",
    data() {
      return {
        menuList:{
          a: {
            id: 1,
            path: "home/user_info"
          }
        }
      }
    }
  };
</script>

<style>
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
  }
</style>
