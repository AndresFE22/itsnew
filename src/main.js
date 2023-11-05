import Vue from 'vue';
import App from './App.vue';
import store from './store'
import vuetify from './plugins/vuetify';
import router from './router'


Vue.config.productionTip = false



router.beforeEach((to, from, next) => {
  const isLoggedIn = localStorage.getItem('isLoggedIn');
  console.log('isLoggedIn:', isLoggedIn); // Agrega este console.log para verificar 
    if ( isLoggedIn && to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.state.auth) {
      next();
    } else {
      next({ name: "Home" });
    }
  } else {
    next();
  }
});

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')