<template>
  <div>
    <v-container>
      <v-row class="text-center" style="margin-top: 350px">
        <v-col class="mb-4">
          <h1 class="display-2 font-weight-bold mb-3">
            닉네임을 입력해주세요<br />
            Please input your nickname
          </h1>
        </v-col>

        <v-col class="mb-5" cols="12" style="">
          <div class="form-group">
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              v-model="name"
              maxlength="6"
              hint="최대 6글자"
              style="font-size:50px" 
              clearable
              @keyup.enter="register"
            />
          </div>
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
          score: 21000,
          city: "N",
        };
        axios.post(url, param)
        .then(function (response) {
          vm.move();
        })
        .catch(function(response){
          Swal.fire({
          icon: "warning",
          html: "<h2>중복된 닉네임입니다. 닉네임을 다시 입력해주세요</h2>",
        });
        })
      }
    },
  },
};
</script>

<style scoped></style>
