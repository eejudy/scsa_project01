<template>
  <v-container>
    <v-row class="text-center" style="margin-top: 100px">
      <v-col class="mb-4">
        <div class="card-group">
          <div
            class="card"
            style="margin-left: 50px;"
            v-for="(item, idx) in topRankers"
          >
          <div v-if="item.username==username" style="background-color: rgba(65, 132, 234, 0.75);">
            <v-img
            v-if="topRankers.length==1"
              :src="require(`../assets/rank/n${idx+2}.png`)"
              height="100"
            />
            <v-img
            v-else-if="topRankers.length==2"
              :src="require(`../assets/rank/n${idx+1}.png`)"
              height="100"
            />
            <v-img
            v-if="topRankers.length>=3"
              :src="require(`../assets/rank/${idx + 1}.png`)"
              height="100"
            />
            <div class="card-body" style="color:white">
              <h1>{{ item.username }}</h1>
              <br />
              <h4 class="card-text" style="color: white">
                {{ item.score }}점
              </h4>
            </div>
          </div>

          <div v-else>
            <v-img
            v-if="topRankers.length==1"
              :src="require(`../assets/rank/n${idx+2}.png`)"
              height="100"
            />
            <v-img
            v-else-if="topRankers.length==2"
              :src="require(`../assets/rank/n${idx+1}.png`)"
              height="100"
            />
            <v-img
            v-if="topRankers.length>=3"
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
            <tbody v-for="(item, idx) in rankers">
              <tr v-if="item.username==username" style="background-color: rgba(65, 132, 234, 0.75);">
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
        let data = response.data
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
