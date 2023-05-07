<template>
<div id='my_div'>
  <v-container class="container">
<!-- <input id='my_btn' type='button' value='clear' /> -->
<!-- <div id='result'>
</div> -->
    <div class="main" @click="mouseClick($event)"></div>
    <v-img
      :src="require('../assets/soccer.png')"
      class="soccer"
      id="soccer"
      contain
      height="100"
      style="margin-top: -300px; margin-right: 0px"
    />
  <img class="mouse-img" id="goal"
    :src="require('@/assets/goal.png')" />

    <canvas
      id="drawCanvas"
      width="2000"
      height="2000"
      style="margin-top: -2000px"
    >
    </canvas>
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
    canvas.onclick = function (event) {
      // console.log(" right container 마우스 클릭!");
      // console.log(event);
      // console.log(event.clientX);
      // console.log(event.clientY);

      let xPosition = event.offsetX -1200 + "px";
      let yPosition = event.offsetY  + "px";
      console.log(xPosition, yPosition);

      let soccer = document.getElementById("soccer");
      soccer.style.left = xPosition
      soccer.style.top =yPosition
      // soccer.style.left =0+"px";
      // soccer.style.top = 1070+"px";
    };


//     const div = document.getElementById('my_div');
// const btn = document.getElementById('my_btn');
// const result = document.getElementById('result');

// div.addEventListener('click', (e) => {
//     result.innerHTML = `<div>screenX, Y: (${e.screenX}, ${e.screenY})</div>`;
//     result.innerHTML += `<div>clientX, Y: (${e.clientX}, ${e.clientY})</div>`;
//     result.innerHTML += `<div>pageX, Y: (${e.pageX}, ${e.pageY})</div>`;
//     result.innerHTML += `<div>offsetX, Y: (${e.offsetX}, ${e.offsetY})</div>`;
// });

// btn.addEventListener('click', (e) => {
// 	result.innerHTML= '';
// });
  },
  data: () => ({
    name: "",
  }),
  methods: {
    move: function () {
      //닉네임 입력 화면으로 이동
      this.$router.push("/intro");
    },
    mouseClick(event) {
      console.log(" right container 마우스 클릭!");
      console.log(event);
      console.log(event.clientX);
      console.log(event.clientY);

      this.xPosition = event.clientX - event.offsetX + "px";
      this.yPosition = event.clientY - event.offsetY + "px";

      console.log(this.xPosition);
      console.log(this.yPosition);
    },
  },
};
</script>

<style scoped>
/* .mouse-img { */

  /* width: 100px; */
  /* height: 100px; */
  /* margin: 0 auto; */

  /* background-image: url("@/assets/goal.png"); */
  /* background-repeat: no-repeat; */
  /* background-position: center center; */
  /* background-size: 1500px; */
  /* background-size: cover;  */
/* } */
.soccer {
  margin-top: 340px;
  margin-right: 870px;
}
.container {
  height: 100vh;
  width: 100vw;
}
 .mouse-img {
   width: 100%;
    margin: auto;
    display: block;
    margin-top:350px;
} 
</style>
