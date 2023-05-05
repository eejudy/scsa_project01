<template>
  <v-toolbar color="info">
    <v-toolbar-title><h1 style="cursor:pointer" @click="move">WGA</h1></v-toolbar-title>
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
