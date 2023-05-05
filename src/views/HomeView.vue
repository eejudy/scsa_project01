<template>
  <div>
    <v-container>
      <v-row class="text-center" style="margin-top: 150px">
        <v-col class="mb-4">
          <h1 class="display-2 font-weight-bold mb-3">게임 방법 소개</h1>
        </v-col>

        <v-col class="mb-5" cols="12">
          <p class>
            당신이 찬 공을 AI가 막을 수 있을까요?<br />
            공을 넣는다면 점수를 획득하고, 계속 게임을 진행할 수 있습니다.<br />
            랭킹에 있는 유저들보다 높은 점수를 획득하면 명예의 전당에 오를 수
            있습니다!
          </p>
          <div class="buttons">
            <button @click="move" class="btn-hover color-9">
              인간 VS AI 시작
            </button>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// import $ from 'jquery'
export default {
  name: "IntroView",

  data: () => ({
    name: "",
  }),
  methods: {
    move: function () {
      this.$router.push("/game");
    },
  },
};
</script>

<style scoped>
.buttons{
  margin-top: 50px;
}
</style>
