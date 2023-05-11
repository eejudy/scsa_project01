<template>
  <v-container class="container">
    <div class="buttons">
      <h2 v-if="targetScore <= score && score != 0">
        명예의 전당에 올랐습니다!
      </h2>
      <h2 v-else>
        {{ targetScore - score }}점 획득시 명예의 전당에 오를 수 있습니다!
      </h2>
    </div>

    <div class="buttons">
      <div class="card">
        <div class="card-body">
          <v-img
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
  created() {
    const vm = this;
    vm.callF();
    vm.getScore();
  },
  data: () => ({
    result: [],
    name: "",
    isFalse: true,
    score: 0,
    targetScore: 0,
    numList: [1, 2, 3, 4, 5, 6, 7],
    toggle: null,
    name: localStorage.getItem("username"),
    img: localStorage.getItem("img"),
  }),
  methods: {
    getScore() {
      let url = "http://127.0.0.1:8000/min_score/";
      const vm = this;
      axios.get(url).then(function (response) {
        vm.targetScore = response.data;
      });
    },
    move: function () {
      //닉네임 입력 화면으로 이동
      this.$router.push("/intro");
    },
    callF() {
      const vm = this;
      let url = "http://127.0.0.1:8000/predict/";
      let param = {
        start: true,
      };
      axios
        .post(url, param)
        .then(function (response) {
          let num = response.data;
          // console.log("최초", num);
          vm.isFalse = false;
          vm.result.push(num);
        })
        .catch(function (response) {
          console.log("fail");
        });
    },
    getData(item) {
      let url = "http://127.0.0.1:8000/predict/";
      const vm = this;
      vm.isFalse = true;
      let param = {
        num: item,
        start: false,
      };

      axios
        .post(url, param)
        .then(function (response) {
          let num = response.data;
          // console.log("다음", num);
          vm.isFalse = false;
          vm.result.push(num);
        })
        .catch(function (response) {
          console.log("fail");
        });
    },
    save() {
      let url = "http://127.0.0.1:8000/user/";
      const vm = this;
      let param = {
        username: vm.name,
        score: vm.score,
      };
      axios
        .post(url, param)
        .then(function (response) {
          console.log(response);
        })
        .catch(function (response) {
          console.log("fail");
        });
    },
    goal(item) {
      const vm = this;
      vm.getData(item);
      let num = this.result.shift();
      if (item != num) {
        let imgArray = new Array();
        imgArray[0] = "04";
        imgArray[1] = "05";
        let imgNum = Math.round(Math.random() * 1);
        let target = imgArray[imgNum];
        intro.setAttribute("src", require(`@/assets/game/g${item}.png`));
        setTimeout(
          () =>
            intro.setAttribute("src", require(`@/assets/game/${target}.png`)),
          1000
        );
        vm.score += 10;
      } else {
        vm.isFalse = true;
        intro.setAttribute("src", require(`@/assets/game/g${item}.png`));
        setTimeout(
          () => intro.setAttribute("src", require("@/assets/game/03.png")),
          1000
        );
        const target = document.getElementById("all_btn");
        target.disabled = true;
        // 사용자 정보 DB에 저장
        vm.save();
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

button {
  font-size: 50px;
  width: 185px;
  margin-top: 50px;
}

.v-btn-group .v-btn {
  border-radius: 0;
  border-color: rgba(65, 132, 234, 0.75);
  border-width: 3px;
}
</style>
