<template>
  <v-container id="particle">
    <v-row class="text-center" style="margin-top: 100px">
      <v-col class="mb-4">
        <div class="card-group">
          <div
            class="card"
            style="margin-left: 50px"
            v-for="(item, idx) in topRankers"
            v-bind:key="`${item}`"
          >
            <div
              v-if="item.username == username"
              style="background-color: rgba(65, 132, 234, 0.75)"
            >
              <v-img
                v-if="topRankers.length == 1"
                :src="require(`../assets/rank/n${idx + 2}.png`)"
                height="100"
              />
              <v-img
                v-else-if="topRankers.length == 2"
                :src="require(`../assets/rank/n${idx + 1}.png`)"
                height="100"
              />
              <v-img
                v-if="topRankers.length >= 3"
                :src="require(`../assets/rank/${idx + 1}.png`)"
                height="100"
              />
              <div class="card-body" style="color: white">
                <h1>{{ item.username }}</h1>
                <br />
                <h4 class="card-text" style="color: white">
                  {{ item.score }}점
                </h4>
              </div>
            </div>

            <div v-else>
              <v-img
                v-if="topRankers.length == 1"
                :src="require(`../assets/rank/n${idx + 2}.png`)"
                height="100"
              />
              <v-img
                v-else-if="topRankers.length == 2"
                :src="require(`../assets/rank/n${idx + 1}.png`)"
                height="100"
              />
              <v-img
                v-if="topRankers.length >= 3"
                :src="require(`../assets/rank/${idx + 1}.png`)"
                height="100"
              />
              <div class="card-body">
                <h1>{{ item.username }}</h1>
                <br />
                <h4 class="card-text" style="color: #3f86ed">
                  {{ item.score }}점
                </h4>
              </div>
            </div>
          </div>
        </div>
      </v-col>
    </v-row>

    <v-row class="text-center" style="margin-top: 100px">
      <v-col class="mb-4">
        <div class="card-group">
          <table class="table">
            <thead>
              <tr>
                <th scope="col">순위</th>
                <th scope="col">닉네임</th>
                <th scope="col">점수</th>
              </tr>
            </thead>
            <tbody v-for="(item, idx) in rankers"      v-bind:key="`${item}`">
              <tr
                v-if="item.username == username"
                style="background-color: rgba(65, 132, 234, 0.75)"
              >
                <td>{{ idx + 4 }}</td>
                <td>{{ item.username }}</td>
                <td>{{ item.score }}점</td>
              </tr>
              <tr v-else>
                <td>{{ idx + 4 }}</td>
                <td>{{ item.username }}</td>
                <td>{{ item.score }}점</td>
              </tr>
            </tbody>
          </table>
        </div>
      </v-col>
    </v-row>

    <div class="buttons">
      <h1>{{ username }}님은 {{ myRank }}위입니다.</h1>
    </div>
    <div class="buttons">
      <button @click="move" class="btn-hover color-9">홈으로 이동</button>
    </div>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  name: "Game",
  mounted() {
    const vm = this
    class Particle {
      constructor(id, opt) {
        this.box = document.getElementById(id);
        this.number = opt.number || 100;
        this.colors = this.handleArrayParams(opt.colors) || [
          "#400606",
          "#c7b4aa",
          "#ffffff",
        ];
        this.width = opt.width || 15;
        this.height = opt.height || 7;
        this.duration = opt.duration || 6000;
        this.delay = opt.delay || 6000;
      }
      handleArrayParams(arr) {
        return Array.isArray(arr) &&
          arr.length > 0 &&
          arr.every((el) => el[0] === "#")
          ? arr
          : false;
      }
      getRandom(max, min = 0) {
        min = Math.ceil(min);
        max = Math.floor(max + 1);
        return Math.floor(Math.random() * (max - min)) + min;
      }
      getRange(num, range = 0.5) {
        const symbol = Math.random() > 0.5 ? +1 : -1;
        return num + this.getRandom(Math.floor(num * range)) * symbol;
      }
      start() {
        for (let i = 0; i < this.number; i++) {
          const temp = document.createElement("span");
          temp.style.cssText += `
        position: absolute;
        transform-style: preserve-3d;
        animation-timing-function: cubic-bezier(${
          this.getRandom(3) * 0.1
        }, 0, 1, 1);
        animation-iteration-count: infinite;
        width: ${this.getRange(this.width, 0.7)}px;
        height: ${this.getRange(this.height, 0.7)}px;
        top: -${this.width * 2}px;
        left: calc(${this.getRandom(100)}% - ${this.width * 0.5}px);
        background-color: ${
          this.colors[this.getRandom(this.colors.length - 1)]
        };
        animation-name: fallen_${this.getRandom(5, 1)};
        animation-duration: ${this.getRange(this.duration)}ms;
        animation-delay: ${this.getRange(this.delay)}ms;
       `;
          this.box.append(temp);
        }
      }
    }
      const party = new Particle("particle", {
        number: 200,
        colors: ["asd", "bdfs"],
      });
      party.start();
  },
  created() {
    const vm = this;
    vm.getData();
    vm.getMyRank();
  },
  data: () => ({
    name: "",
    rankers: [],
    topRankers: [],
    myRank: 0,
    username: "",
  }),
  methods: {
    move: function () {
      this.$router.push("/");
    },
    getData() {
      let url = "http://127.0.0.1:8000/user/";
      const vm = this;
      axios.get(url).then(function (response) {
        let data = response.data;
        for (var i = 0; i < data.length; i++) {
          if (i == 1) {
            vm.topRankers.unshift(data[i]);
          } else if (i < 3) {
            vm.topRankers.push(data[i]);
          } else {
            vm.rankers.push(data[i]);
          }
        }
      });
    },
    getMyRank() {
      let url = "http://127.0.0.1:8000/rank/";
      const vm = this;
      axios.get(url).then(function (response) {
        vm.myRank = response.data.cnt;
        vm.username = response.data.username;
      });
    },
  },
};
</script>

<style scoped>
th,
td {
  text-align: center;
}
</style>

<style lang="scss">
.body {
  width: 100vw;
  height: 100vh;
  background: #212121;
}
@function randomNum($min, $max) {
  $rand: random();
  $randomNum: $min + floor($rand * (($max - $min) + 1));
  $bool: random();
  @if ($bool > 0.5) {
    $randomNum: $randomNum * -1;
  }
  @return $randomNum;
}
@for $i from 1 through 5 {
  @keyframes fallen_#{$i} {
    100% {
      top: calc(100% + 20px);
      transform: rotateX(#{randomNum(360, 1440)}deg)
        rotateY(#{randomNum(360, 1440)}deg) rotateZ(#{randomNum(360, 1440)}deg);
    }
  }
}
</style>
