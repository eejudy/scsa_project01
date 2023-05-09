<template>
  <v-toolbar color="info">
    <v-toolbar-title><h1 style="cursor:pointer" @click="move">
      <v-img
          @click="move"
          :src="require(`../assets/logo/scsa_WGA2.png`)"
          height="100"
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
