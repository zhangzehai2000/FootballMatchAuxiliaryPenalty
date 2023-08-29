<template>

  <div>
    <div class="videoContainer" >
      <video class="fullscreenVideo" id="bgVid" playsinline="" autoplay="" muted="" loop="">
        <source src="../../../assets/video/bg1.mp4">
      </video>
    </div>

      <h2></h2>
      <div class="login_context" @click="toggle()":style="opacity">

        <!-- 这里放图片logo -->
        <div class="login_logo">
          <img src="../../../assets/1.png" alt="" />

        </div>

        <el-form :model="loginRuleForm" :rules="loginRules" ref="loginRules" class="login_box">

          <el-form-item label="账号" prop="username" >
            <el-input v-model="loginRuleForm.username" @focus="toggle_2()"></el-input>
          </el-form-item>

          <el-form-item label="密码" prop="password" >
            <el-input v-model="loginRuleForm.password" @focus="toggle_2()"></el-input>
          </el-form-item>

          <el-form-item class="btns">
            <el-button type="primary" @click="login" >登陆</el-button>
          </el-form-item>
        </el-form>

    </div>
  </div>

</template>

<script>
  // Vue 代码逻辑
  export default {
    data() {
      return {
        opacity: "opacity:0.35",
        greeting: " ",

        // 表单请求数据
        loginRuleForm: {
          username: '',
          password: '',
        },
        // 表单验证规则
        loginRules: {
          username: [{
              required: true,
              message: "请输入用户名",
              trigger: "blur"
            },
            {
              min: 3,
              max: 18,
              message: "长度在 3 到 18 个字符",
              trigger: "blur",
            },
          ],
          password: [{
              required: true,
              message: "请输入密码",
              trigger: "blur"
            },
            {
              min: 3,
              max: 18,
              message: "长度在 3 到 18 个字符",
              trigger: "blur",
            }
          ]
        }
      };
    },
    methods: {
      toggle() {
        if (this.opacity === "opacity:0.35") {
          this.opacity = "opacity:85";
        } else {
          this.opacity = "opacity:0.35";
        }
      },
      toggle_1() {
        this.opacity = "opacity:0.85";
      },
      toggle_2() {
        this.opacity = "opacity:0.35";
      },


      login() {
        // 登陆进行规则的校验，只有校验成功才能登陆
        // vaild=>所有的规则校验都成立才会进入到这里
        this.$refs.loginRules.validate((vaild) => {
          if (!vaild) return;
          // 直接请求数据，格式是payload，如果服务端要求是payload格式那么这样请求
          // this.$axios.post("http://192.168.17.176:8089/login", this.loginRuleForm).then((res) => {
          //   console.log(res)
          // })

          // 请求数据，格式是formdata，需要添加 this.qs.stringify()进行格式转换
          // this.$axios.post("http://172.25.36.101:8091/login", this.qs.stringify(this.loginRuleForm)).then((
          //   res) => {
          //   console.log(res)

            // if (res.data.code != 0 && res.data.code != 401) {
            //   return this.$message.error(res.data.msg);
            // }


            // 跳转到主页
            this.$router.push("/home");
            this.$message.success("HI! " + this.loginRuleForm.username + " 欢迎使用足球比赛辅助判罚系统！");

          })

      }
    }
  }
</script>

<style scoped>

  .videoContainer{
    position: fixed;
    width: 100%;
    height: 100%;
    overflow: hidden;
    z-index: -100;
  }

  .videoContainer:before{
    content: "";
    position: absolute;
    width: 100%;
    height: 100%;
    display: block;
    z-index: -1;
    top: 0;
    left: 0;
    background: rgba(25,29,34,.65);
  }


  .login {
    /* 高度 */
    height: 100%;
    /* 背景色 */
    background: rgb(242, 244, 247);

  }

  .login_title {
    /* 字体水平左右居中 */
    text-align:center;
  }

  .login_context {
    /*透明度*/
    /* background-color: #ffffff; */
    background: rgba(255,255,255,0.3);
    /*border: 1px solid black;*/
    /*opacity: 0.3;*/
    filter: alpha(opacity=90);

    /* 宽度 */
    width: 450px;
    /* 高度 */
    height: 300px;
    /* 背景色 */
    background: #fff;
    /* 属性定位 */
    position: absolute;
    /* 属性定位，顶部占比 */
    top: 50%;
    /* 属性定位，左侧占比 */
    left: 50%;
    /* 水平垂直居中 */
    transform: translate(-50%, -50%);
    /* 四个角的圆角角度 */
    border-radius: 20px;
    /* 阴影 */
    box-shadow: 0 0 5px 2px #ddd;
  }

  .login_logo {
    /* 宽度 */
    width: 150px;
    /* 高度 */
    height: 150px;
    /* 属性定位 */
    position: absolute;
    /* 属性定位，顶部占比 */
    top: -75px;
    /* 属性定位，左侧占比 */
    left: 49%;
    /* logo左侧边距 */
    margin-left: -75px;
    /* 带有边框属性 */
    border: 1px solid #eee;
    /* 四个角的圆角角度 */
    border-radius: 50%;
    /* 背景色 */
    background: #fff;
    /* 设置内边距属性 */
    padding: 10px;
    /* 阴影 */
    box-shadow: 0 0 2px 2px #ddd;
  }

  .login_logo img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: rgb(238, 238, 238);
  }

  .login_box {
    width: 100%;
    position: absolute;
    bottom: 0;
    padding: 0 50px;
    /* 边框边距 */
    box-sizing: border-box;
  }

  .btns {
    /* 将对象作为弹性伸缩盒显示 */
    display: flex;
    /* 横轴方向上的对齐方式 */
    justify-content: flex-end;
  }
</style>
