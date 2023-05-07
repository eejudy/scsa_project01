<template>
  <v-container class="container">
    <img class="mouse-img" id="goal" :src="require('@/assets/goal.png')" />
    <v-row class="text-center" style="margin-top: 50px">
      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3"></h1>
        <!-- <div
          class="btn-group"
          role="group"
          style="width:170px;height:100px;"
          aria-label="Basic checkbox toggle button group"
          v-for="(item, idx) in numList"
        > -->
        <div style="width:170px;height:100px;" v-for="(item, idx) in numList" class="btn-group" role="group" aria-label="Basic checkbox toggle button group">
          <!-- <input
            type="checkbox"
            class="btn-check"
            v-bind:id="`btn${item}`"
            autocomplete="off"
          /> -->
           <button style="font-size:50px;" v-bind:id="`btn${item}`" type="button" class="btn btn-outline-primary">{{item}}</button>
          <!-- <label style="font-size:50px;" class="btn btn-outline-primary" :for="`btn${item}`">{{item}}</label> -->
        </div>
        
 <div>
    <v-btn-toggle
      v-model="toggle"
      color="info"
      variant="outlined"
      style="height:150px;" 
    >
        <v-btn  style="font-size:50px;width:170px;" v-bind:id="`btn${item}`" v-for="(item, idx) in numList" >{{item}}</v-btn>
      
  
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
    numList: [1,2,3,4,5,6,7],
    toggle:null,
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
/* .mouse-img { */

/* width: 100px; */
/* height: 100px; */
/* margin: 0 auto; */

/* background-image: url("@/assets/goal.png"); */
/* background-repeat: no-repeat; */
/* background-position: center center; */
/* background-size: 1500px; */
/* background-size: cover;  */
/* } */
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
