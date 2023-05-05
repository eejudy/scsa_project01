<template>
  <div>
    <v-container>
      <v-row class="text-center" style="margin-top: 150px">
        <v-col class="mb-4">
          <h1 class="display-2 font-weight-bold mb-3">명예의 전당</h1>
          <table class="table" style="margin-top: 100px">
            <tbody>
              <tr v-for="(item, idx) in rankers">
                <th v-if="idx < 3" scope="row">
                  <v-img
                    :src="require(`../assets/${idx + 1}.png`)"
                    height="80"
                  />
                </th>
                <th v-else scope="row">{{ idx + 1 }}</th>
                <td>{{ item.username }}</td>
                <td>{{ item.age }}점</td>
              </tr>
            </tbody>
          </table>
          <div class="buttons">
            <button @click="move" class="btn-hover color-9">홈으로 이동</button>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
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
    users: [
      { nickname: "강아지", score: "1000" },
      { nickname: "고양이", score: "800" },
      { nickname: "라마", score: "500" },
      { nickname: "알파카", score: "450" },
      { nickname: "짱구", score: "400" },
      { nickname: "흰둥이", score: "300" },
      { nickname: "철이", score: "200" },
    ],
  }),
  methods: {
    move: function () {
      this.$router.push("/");
    },
    getData() {
      let url = "http://127.0.0.1:8000/user/";
      const vm = this;
      axios.get(url).then(function (response) {
        vm.rankers = response.data;
      });
    },
  },
};
</script>

<style scoped>
.table {
  background-color: aliceblue;
}
</style>
