<template>
  <div class="main">
    <v-container>
      <canvas
        id="drawCanvas"
        @click="showColor(e)"
        width="200"
        height="200"
        style="margin-top:300px;"
      ></canvas>
      <v-row class="text-center" style="margin-top: 300px">
        <v-col class="mb-4">
          <h1 class="display-2 font-weight-bold mb-3"></h1>
          <div class="buttons">
            <button
              @click="move"
              style="visibility: hidden"
              class="btn-hover color-9"
            ></button>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// import $ from 'jquery'
export default {
  name: "Game",
  mounted() {
    var canvas = document.getElementById("drawCanvas");
    var ctx = canvas.getContext("2d");
    ctx.fillStyle = "rgb(200,0,0)";
    ctx.fillRect(10, 10, 50, 50);
},
  data: () => ({
    name: "",
  }),
  methods: {
    move: function () {
      //닉네임 입력 화면으로 이동
      this.$router.push("/intro");
    },
  },
};
</script>

<style scoped>
.main {
  background-image: url("@/assets/goal.jpg");
  background-size: cover;
}
</style>
