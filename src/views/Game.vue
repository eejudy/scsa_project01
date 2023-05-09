<template>
  <v-container class="container">
    <div class="buttons">
      <button>
        <div class="card" style="width: 350px">
          <div class="card-body">
            <v-img
              @click="select(item)"
              :src="require(`../assets/character/${img}.png`)"
              height="100"
            />
            <h5
              class="card-title mb-9 fw-semibold"
              align="center"
              style="margin-top: 20px"
            >
              {{ name }}님의 점수
            </h5>
            <h3 align="center">{{ score }}점</h3>
          </div>
        </div>
      </button>
    </div>
    <img class="mouse-img" id="goal" :src="require('@/assets/game/02.png')" />
    <img class="mouse-img" id="goal" :src="require('@/assets/game/goal.png')" />
    <v-row class="text-center" style="margin-top: 50px">
      <v-col class="mb-4">
        <div>
          <v-btn-toggle
            v-model="toggle"
            color="info"
            variant="outlined"
            style="height: 150px"
            id="all_btn"
            >
            <v-btn
              @click="goal(item)"
              style="font-size: 50px; width: 180px"
              v-bind:id="`btn${item}`"
              v-for="item in numList"
              v-bind:key="`btn${item}`"
              >{{ item }}</v-btn
            >
          </v-btn-toggle>
        </div>
        <!-- <div class="buttons">
          <button @click="move" class="btn-hover color-9">닉네임 등록</button>
        </div> -->
      </v-col>
    </v-row>
  </v-container>

  <!-- <div class="body-wrapper" style="margin-top:100px;">
      <div class="container-fluid">
        <div class="row">
          <div class="col-lg-8 d-flex align-items-strech">
            <div>
                  <img class="mouse-img" id="goal" :src="require('@/assets/goal.png')" />
              <div class="card-body">
                <div class="d-sm-flex d-block align-items-center justify-content-between mb-9">
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-4">
            <div class="row">
              <div class="col-lg-12">
                <div class="card overflow-hidden">
                  <div class="card-body p-4">
                    <h5 class="card-title mb-9 fw-semibold">점수</h5>
                    <div class="row align-items-center">
                      <div class="col-8">
                        <h4 class="fw-semibold mb-3">{{score}}</h4>
                       
                        
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-12" style="margin-top:20px">
                <div class="card">
                  <div class="card-body">
                    <div class="row alig n-items-start">
                      <div class="col-8">
                        <h5 class="card-title mb-9 fw-semibold"> Monthly Earnings </h5>
                        <h4 class="fw-semibold mb-3">$6,820</h4>
                        <div class="d-flex align-items-center pb-1">
                          <span
                            class="me-2 rounded-circle bg-light-danger round-20 d-flex align-items-center justify-content-center">
                            <i class="ti ti-arrow-down-right text-danger"></i>
                          </span>
                          <p class="text-dark me-1 fs-3 mb-0">+9%</p>
                          <p class="fs-3 mb-0">last year</p>
                        </div>
                      </div>
                      <div class="col-4">
                        <div class="d-flex justify-content-end">
                          <div
                            class="text-white bg-secondary rounded-circle p-6 d-flex align-items-center justify-content-center">
                            <i class="ti ti-currency-dollar fs-6"></i>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div id="earning"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div> -->
</template>

<script>
// import $ from 'jquery'
export default {
  name: "Game",
  mounted() {},
  data: () => ({
    name: "",
    score: 0,
    numList: [1, 2, 3, 4, 5, 6, 7],
    toggle: null,
    name: localStorage.getItem("username"),
    img: localStorage.getItem("img"),
  }),
  methods: {
    move: function () {
      //닉네임 입력 화면으로 이동
      this.$router.push("/intro");
    },
    goal(item) {
      const vm = this;
      let num = 3;
      console.log(item);
      if (item != num) {
        // Swal.fire({
        //   icon: "success",
        //   html: "<h2>GOAL!</h2>",
        // });

        const goal = document.getElementById("goal");
        goal.setAttribute("src", require("@/assets/character/meowth.png"));
        vm.score += 10;
      } else {
        // Swal.fire({
        //   icon: "error",
        //   html: "<h2>골키퍼가 공을 막았습니다</h2>",
        // });
        const target = document.getElementById("all_btn")
        target.disabled = true;
        setTimeout(() => this.$router.push("/rank"), 2000);
      }
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
  /* width: 990px; */
  /* height:490px; */
  display: block;
}
</style>
