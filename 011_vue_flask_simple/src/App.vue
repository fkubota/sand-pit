<template>
  <v-app>
    <v-card width='400px' class='mx-auto mt-4'>
      <v-card-title>
        <h1 class="display-1">{{msg}}</h1>
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-card-actions>
            <v-btn class='info' v-on:click='connect_api'>ログイン</v-btn>
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
    val_app_vue: 'text_app_vue',
	to_api: ''
  }),
  methods: {
    disp(){
      this.msg = 'hhh'
    },
    connect_api(){
      console.log('----- begin vue -----')
      axios.post('http://127.0.0.1:5000/myapi', {
        arg1: this.val_app_vue
      })
      .then((response) => {
        this.to_api = response.data.AA
      })
    }
  }
  };
</script>
