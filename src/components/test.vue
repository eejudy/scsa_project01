<template>
  <v-container fluid>
      <v-layout column>
        <v-flex xs12>
            <h3 class="subject">User CRUD</h3>
        </v-flex>
        <v-flex column>
          <v-row>
            <v-col cols="4" md="4">
              <v-text-field v-model="username" :counter="15" label="Username" required></v-text-field>
            </v-col>
             <v-col cols="4" md="4">
              <v-text-field v-model="age" label="Age" required></v-text-field>
            </v-col>
             <v-col cols="4" md="4">
              <v-text-field v-model="city" :counter="15" label="City" required></v-text-field>
            </v-col>
          </v-row>
            <v-form ref="form" v-model="valid" lazy-validation>
            <v-btn @click="create" style="background:green">create</v-btn>
             <v-btn @click="clear" style="background:red">clear</v-btn>
            </v-form>
        </v-flex>

        <v-flex class="userList" column>
          <v-card max-width="600" tile>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Title</v-list-item-title>
                  <v-list-item-subtitle>content</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-card>

        </v-flex>
      </v-layout>
    
  </v-container>
</template>

<script>

export default {
  name: 'test',

  data: () => ({ 
  }),
  methods:{
  }
  }
</script>

<style>
.subject{
  color:blue;
  font-style:oblique;
  padding:30px;
  text-align:center;
}

.userList{
  margin: 30px 0px 30px 0px;
}
</style>