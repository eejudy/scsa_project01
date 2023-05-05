<template>
  <div>
    <v-container>
      <v-row class="text-center" style="margin-top: 300px">
        <v-col class="mb-4">
          <h1 class="display-2 font-weight-bold mb-3">게임 화면</h1>
          <div class="buttons">
            <button @click="move" class="btn-hover color-9">이동</button>
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
.v-main {
  background-image: url("@/assets/goal.jpg");
}
</style>
