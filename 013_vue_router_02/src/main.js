import Vue from "vue";
import App from "./App";
import router from './router.js'

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router, // アプリケーションに登録
  render: h => h(App)
})
