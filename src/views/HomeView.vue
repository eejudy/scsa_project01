<template>
  <div class="container">
    <v-container>
      <v-row class="text-center" style="margin-top: 200px">
        <v-col class="mb-4">
          <h1 class="display-2 font-weight-bold mb-3">닉네임을 입력해주세요</h1>
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
              style="font-size: 50px"
              clearable
              @keyup.enter="register"
            />
          </div>

          <v-row class="text-center" style="margin-top: 100px">
            <v-col class="mb-4">
              <h1 class="display-2 font-weight-bold mb-3">
                캐릭터를 선택해주세요
              </h1>
              <div class="py-5">
                <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3">
                  <div class="col" v-for="item in characters" v-bind:key="item">
                    <div class="card">
                      <v-img
                        @click="select(item)"
                        style="cursor: pointer"
                        :src="require(`../assets/character/${item}.png`)"
                        v-bind:id="`${item}`"
                        height="100"
                      />
                    </div>
                  </div>
                </div>
                <div class="buttons">
                  <button @click="enter" class="btn-hover color-9">
                    입장하기
                  </button>
                </div>
              </div>
            </v-col>
          </v-row>
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
    img: "",
    preSelect: null,
    characters: [
      "pikachu",
      "bullbasaur",
      "charmander",
      "meowth",
      "eevee",
      "jigglypuff",
    ],
  }),
  methods: {
    check() {
      if (this.name.length == 0) {
        Swal.fire({
          icon: "warning",
          html: "<h2>닉네임을 입력해주세요</h2>",
        });
        return false;
      }

      if (this.img.length == 0) {
        Swal.fire({
          icon: "warning",
          html: "<h2>캐릭터를 선택해주세요</h2>",
        });
        return false;
      }

      return true;
    },
    enter() {
      if (this.check()) {
        const vm = this;
        let url = "http://127.0.0.1:8000/check_duplicate/";
        let param = { currIN: vm.name };
        axios.post(url, param).then(function (response) {
          if (response.data.check) {
            localStorage.setItem("username", vm.name);
            localStorage.setItem("img", vm.img);
            vm.$router.push("/intro");
          } else {
            Swal.fire({
              icon: "warning",
              html: "<h2>중복된 닉네임입니다. 다시 입력해주세요.</h2>",
            });
          }
        });
      }
    },
    move: function () {
      this.$router.push("/rank");
    },
    select(item) {
      this.img = item;
      if (this.preSelect != null) {
        let preImg = document.getElementById(this.preSelect);
        preImg.style.backgroundColor = "white";
      }
      let img = document.getElementById(item);
      img.style.backgroundColor = "skyblue";
      this.preSelect = item;
    },
  },
};
</script>

<style scoped></style>
