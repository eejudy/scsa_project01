<template>
  <v-container>
    <v-row class="text-center" style="margin-top: 100px">
      <v-col class="mb-4">
        <div class="card-group">
          <div
            class="card"
            style="margin-left: 50px"
            v-for="(item, idx) in topRankers"
          >
            <v-img :src="require(`../assets/${idx + 1}.png`)" height="100" />
            <div class="card-body">
              <h1>{{ item.username }}</h1><br>
              <h4 class="card-text" style="color:#3f86ed">{{ item.score }}점</h4>
            </div>
          </div>
        </div>
      </v-col>
    </v-row>

    <table class="table">
      <thead>
        <tr>
          <th scope="col">순위</th>
          <th scope="col">닉네임</th>
          <th scope="col">점수</th>
        </tr>
      </thead>
      <tbody v-for="(item, idx) in rankers">
        <tr>
          <td>{{ idx + 4 }}</td>
          <td>{{ item.username }}</td>
          <td>{{ item.score }}</td>
        </tr>
      </tbody>
    </table>

    <div class="buttons">
      <button @click="move" class="btn-hover color-9">홈으로 이동</button>
    </div>

    <!-- <div>
      <v-container>
        <v-row class="text-center" style="margin-top: 150px">
          <v-col class="mb-4">
            <table class="table" style="margin-top: 100px">
              <thead>
                <tr>
                  <th>순위</th>
                  <th>닉네임</th>
                  <th>점수</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, idx) in rankers">
                  <td>{{ idx + 4 }}</td>
                  <td>{{ item.username }}</td>
                  <td>{{ item.score }}점</td>
                </tr>
              </tbody>
            </table>
            <div class="buttons">
              <button @click="move" class="btn-hover color-9">
                홈으로 이동
              </button>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </div> -->
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  name: "Game",
  created() {
    const vm = this;
    vm.getData();
  },
  data: () => ({
    name: "",
    rankers: [],
    topRankers: [],
  }),
  methods: {
    move: function () {
      this.$router.push("/");
    },
    getData() {
      let url = "http://127.0.0.1:8000/user/";
      const vm = this;
      axios.get(url).then(function (response) {
        console.log(response);
        for (var i = 0; i < response.data.length; i++) {
          if (i == 1) {
            vm.topRankers.unshift(response.data[i]);
          } else if (i < 3) {
            vm.topRankers.push(response.data[i]);
          } else {
            vm.rankers.push(response.data[i]);
          }
        }
      });
      console.log(vm.topRankers);
      console.log(vm.rankers);
    },
  },
};
</script>

<style scoped>
.table{
  width:1100px; 
  margin-left:660px; 
  margin-top: 150px;
}
</style>
