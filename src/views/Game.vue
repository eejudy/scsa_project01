<template>
  <v-container class="container">
    <div class="buttons">
      <button></button>
    </div>
    
    <!-- <v-btn
              @click="
                play(
                  'http://soundbible.com/mp3/Air Plane Ding-SoundBible.com-496729130.mp3'
                )
              "
            /> -->

    <div class="buttons">
      <div class="card">
        <div class="card-body">
          <v-img
            @click="select(item)"
            :src="require(`../assets/character/${img}.png`)"
            height="100"
          />
          <h5 class="card-title mb-9 fw-semibold" align="center">
            {{ name }}님의 점수
          </h5>
          <h3 align="center">{{ score }}점</h3>
        </div>
      </div>
      <img
        class="mouse-img"
        id="intro"
        :src="require('@/assets/game/02.png')"
      />
      <img
        class="intro-img"
        id="goal"
        :src="require('@/assets/game/goal.png')"
      />
    </div>
    <div class="buttons">
      <div>
        <v-btn-toggle
          v-model="toggle"
          color="info"
          variant="outlined"
          id="all_btn"
          v-bind:disabled="isFalse"
        >
          <v-btn
            @click="goal(item)"
            v-bind:id="`btn${item}`"
            v-for="item in numList"
            v-bind:key="`btn${item}`"
            >{{ item }}</v-btn
          >
        </v-btn-toggle>
      </div>
    </div>
  </v-container>
</template>

<script>
// import $ from 'jquery'
import axios from "axios";
export default {
  name: "Game",
  mounted() {},
  created(){
    const vm = this
    vm.callF()
  },
  data: () => ({
    result: [],
    name: "",
    isFalse: false,
    score: 0,
    numList: [1, 2, 3, 4, 5, 6, 7],
    toggle: null,
    name: localStorage.getItem("username"),
    img: localStorage.getItem("img"),
  }),
  methods: {
    play(sound) {
      var audio = new Audio(sound);
      audio.play();
      // audio.pause();
    },
    move: function () {
      //닉네임 입력 화면으로 이동
      this.$router.push("/intro");
    },
    callF(){
      const vm = this;
      let num = 3
      vm.result.push(num)
    },
    getData() {
      let url = "http://127.0.0.1:8000/result_test/";
      const vm = this
      let param = {
          num: 5
        };
        axios
          .post(url, param)
          .then(function (response) {
            let num = response.data.num
            vm.result.push(num)
          })
          .catch(function (response) {
            console.log('fail')
          });
    },
    goal(item) {
      const vm = this;
      vm.getData()
      let num = this.result.shift();
      console.log(num)
      if (item != num) {
        // Swal.fire({
        //   icon: "success",
        //   html: "<h2>GOAL!</h2>",
        // });
        let imgArray = new Array();
        imgArray[0]="04"
        imgArray[1]="05"
        let imgNum = Math.round(Math.random()*1)
        let target = imgArray[imgNum]
        intro.setAttribute("src", require(`@/assets/game/g${item}.png`));
        setTimeout(() =>  intro.setAttribute("src", require(`@/assets/game/${target}.png`)), 1000);
        vm.score += 10;
      } else {
        vm.isFalse = true
        // Swal.fire({
        //   icon: "error",
        //   html: "<h2>골키퍼가 공을 막았습니다</h2>",
        // });
        intro.setAttribute("src", require(`@/assets/game/g${item}.png`));
        setTimeout(() =>  intro.setAttribute("src", require("@/assets/game/03.png")), 1000);
        const target = document.getElementById("all_btn");
        target.disabled = true;
        setTimeout(() => this.$router.push("/rank"), 2000);
      }
    },
  },
};
</script>

<style scoped>
.card {
  width: 350px;
  float: left;
}
h5 {
  margin-top: 20px;
}

button{
  font-size: 50px; width: 185px; margin-top: 50px
}
</style>