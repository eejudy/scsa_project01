<template>
  <div>
    <v-container>
      <v-row class="text-center" style="margin-top: 150px">
        <v-col class="mb-4">
          <h1 class="display-2 font-weight-bold mb-3">
            닉네임을 입력해주세요<br />
            Please input your nickname
          </h1>
        </v-col>

        <v-col class="mb-5" cols="12" style="margin-top: 0px">
          <v-text-field
            clearable
            ref="name"
            required
            maxlength="20"
            color="blue darken-2"
            v-model="name"
            label=""
            variant="underlined"
            style="font-size: 100px"
          ></v-text-field>
          <div class="buttons">
            <button @click="register" class="btn-hover color-9">
              명예의 전당 등록
            </button>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// import $ from 'jquery'
import axios from "axios";
export default {
  name: "HelloWorld",

  data: () => ({
    name: "",
  }),
  methods: {
    move: function () {
      this.$router.push("/rank");
    },
    register() {
      let url = "http://127.0.0.1:8000/user/";
      const vm = this;
      if (vm.name.length == 0) {
        Swal.fire({
          icon: "warning",
          html: "<h2>닉네임을 입력해주세요</h2>",
        });
      } else {
        let param = {
          username: vm.name,
          age: 100,
          city: "N",
        };
        axios.post(url, param).then(function (response) {
          if (response.status == 201) {
            vm.move();
          }
        });
      }
    },
  },
};
</script>

<style>
.container {
	height: 100vh;
    	width: 100vw;
}
@font-face {
  font-family: "D2Coding";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_three@1.0/D2Coding.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

body {
  font-size: 30px;
  font-family: "D2Coding";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}

.buttons {
  margin: 0%;
  text-align: center;
}

.btn-hover {
  width: 500px;
  font-size: 30px;
  font-weight: 600;
  color: #fff;
  cursor: pointer;
  margin: 20px;
  height: 100px;
  text-align: center;
  border: none;
  background-size: 300% 100%;

  border-radius: 50px;
  moz-transition: all 0.4s ease-in-out;
  -o-transition: all 0.4s ease-in-out;
  -webkit-transition: all 0.4s ease-in-out;
  transition: all 0.4s ease-in-out;
}

.btn-hover:hover {
  background-position: 100% 0;
  moz-transition: all 0.4s ease-in-out;
  -o-transition: all 0.4s ease-in-out;
  -webkit-transition: all 0.4s ease-in-out;
  transition: all 0.4s ease-in-out;
}

.btn-hover:focus {
  outline: none;
}

.btn-hover.color-9 {
  background-image: linear-gradient(
    to right,
    #25aae1,
    #4481eb,
    #04befe,
    #3f86ed
  );
  box-shadow: 0 4px 15px 0 rgba(65, 132, 234, 0.75);
}
.v-text-field input {
  font-size: 50px;
}
</style>
