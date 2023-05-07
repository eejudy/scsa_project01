<template>
  <v-container class="container">
    <div class="card" style="width: 30rem; margin-top: 50px">
      <div class="card-body">
        <h1 class="card-text">점수</h1>
        <p style="margin-left: 10px; margin-top: 20px">{{ score }}</p>
      </div>
    </div>
    <img class="mouse-img" id="goal" :src="require('@/assets/goal.png')" />
    <v-row class="text-center" style="margin-top: 50px">
      <v-col class="mb-4">
        <div>
          <v-btn-toggle
            v-model="toggle"
            color="info"
            variant="outlined"
            style="height: 150px"
          >
            <v-btn
              @click="goal(item)"
              style="font-size: 50px; width: 200px"
              v-bind:id="`btn${item}`"
              v-for="(item, idx) in numList"
              >{{ item }}</v-btn
            >
          </v-btn-toggle>
        </div>
        <div class="buttons">
          <button @click="move" class="btn-hover color-9">닉네임 등록</button>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// import $ from 'jquery'
export default {
  name: "Game",
  mounted() {},
  data: () => ({
    name: "",
    score: 0,
    numList: [1, 2, 3, 4, 5, 6],
    toggle: null,
  }),
  methods: {
    move: function () {
      //닉네임 입력 화면으로 이동
      this.$router.push("/intro");
    },
    goal(item) {
      console.log(item);
    },
  },
};
</script>

<style scoped>
.buttons {
  margin-top: 100px;
}
.soccer {
  margin-top: 340px;
  margin-right: 870px;
}
.container {
  height: 100vh;
  width: 100vw;
}
.mouse-img {
  width: 50%;
  margin: auto;
  display: block;
  margin-top: 50px;
}
</style>
