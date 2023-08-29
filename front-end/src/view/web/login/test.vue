<template>
  <div class="hello">

    <div class="top">
      3楼
    </div>

    <div class="middle" @click="greet()" :style="opacity">
      <div class="bedroom room">
        2楼卧室
      </div>
      <div class="bathroom room">
        2楼洗手间
      </div>
    </div>

    <div class="bottom">
      Floor 3 {{this.greeting}}
    </div>

    <input type="button" @click="toggle()" value="切换">
  </div>
</template>

<script>

  export default {
    data() {
      return {
        opacity: "opacity:1",
        greeting: " "
      };
    },
    methods: {
      greet() {
        this.greeting = "Hello!";
        },
      toggle() {
        if (this.opacity === "opacity:1") {
          this.opacity = "opacity:0";
        } else {
          this.opacity = "opacity:1";
        }
      }
    }
};
</script>

<style scoped>
/* ...  */
.middle {
/* ...  */opacity: 1;
}
.bedroom {
/* ...  */opacity: 1;
}
</style>