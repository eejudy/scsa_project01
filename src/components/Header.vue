<template>
  <v-toolbar color="info">
    <v-toolbar-title><h1 style="cursor:pointer" @click="move">
      <v-img
          @click="move"
          :src="require(`../assets/logo/scsa_WGA2.jpg`)"
          height="80"
          style="margin-top:10px"
        />
    </h1></v-toolbar-title>
  </v-toolbar>
</template>

<script>

export default {
  name: "Header",

  data: () => ({
    name: "",
  }),
  methods: {
    move: function () {
      this.$router.push("/");
    },
  },
};
</script>