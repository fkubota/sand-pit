<template>
  <v-app>
    <v-card width='400px' class='mx-auto mt-4'>
      <v-card-title>
        <h1 class="display-1">{{msg}}</h1>
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-card-actions>
            <v-btn class='info' v-on:click='to_api'>ログイン</v-btn>
          </v-card-actions>
        </v-form>
      </v-card-text>
    </v-card>
  </v-app>
</template>

<script>
  import axios from 'axios'
  export default {
  name: 'App',
  data: () => ({
    msg: 'hello',
  }),
  methods: {
    to_api(){
      console.log('----- begin vue -----')
      axios.post('http://127.0.0.1:5002/myapi', {
        arg01: this.msg
      })
      .then((response) => {
        this.msg = response.data.after_api
      })
    }
  }
  };
</script>
