<template>
  <div class="container" >
    <background-animation />
    <v-container class="home-container" fluid fill-height >
      <v-layout align-center justify-center>
        <v-card class="home-card" elevation="10" >
          <div class="logos">
            <img src="../assets/pngwing.com.png" alt="">
            <img src="../assets/edutlan.jpg" alt=""> 
          </div>
          <v-card-text>
            <h1 class="display-1 line-spacing">
              Welcome to the Intelligent Tutor System! <br> LANGUAGE TUTOR (STILT)
            </h1>
          </v-card-text>
          <v-card-text>
            <h2 class="display-1">
              Topic: Prepositions
            </h2>
          </v-card-text>
          <v-card-text>
            <p class="subtitle-1 line-spacing">We develop your skills for solving problems related to prepositions.</p>
          </v-card-text>
          <v-card-actions>
              <v-btn color="#0084ff" large class="bt" @click="dialog = true">
              <span class="mdi mdi-play-circle"></span> START
            </v-btn>
          </v-card-actions>
          <transition name="fade">
          <div v-if="dialog" class="login-slider">
              <auth :useDiv="false" />
          </div>
        </transition>
        </v-card>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import BackgroundAnimation from "./backgroundAnimation.vue";
/*import login from "./loginU.vue";*/
/*import register from "./registerU.vue"*/
import auth from "../components/HomeView.vue";

export default {
  name: "HomeP",
  data () {
      return {
        dialog: false,
      }
    },
  components: {
    BackgroundAnimation,
    auth
    /*register*/
  },
  watch: {
      dialog (val) {
        if (!val) return
      },
    },  
  methods: {
    startActivity() {
    },
    closeDialog() {
      this.dialog = false;
    },
  },
};
</script>

<style scoped>

@media screen and (max-width: 900px) {
  img {
    width: 100px;

  }
  h1 {
    font-size: 20pt;
    margin-bottom: 25px;
  }

  h2 {
    font-size: 15pt;
    margin-bottom: 15px;
  }

  p {
    font-size: 12pt;
    margin-bottom: 15px;
  }
  .line-spacing {
  line-height: 1.2;
}
}

.container {
  background-color: rgba(0, 0, 0, 0);
}

h1 {
  font-size: 30pt;
  font-weight: bold;
  font-family: 'Roboto', sans-serif;
  color: #0084ff;
  margin-bottom: 20px;
  }

  h2 {
  font-size: 20pt;
  font-weight: bold;
  font-family: 'Roboto', sans-serif;
  color: #727272;
  margin-bottom: 20px;

  }

p {
  font-size: 20pt;
  font-family: 'Roboto', sans-serif;
  margin-bottom: 20px;

}

img {
  width: 200px;
  margin-bottom: 20px;

}

.bt {
  font-family: 'Roboto', sans-serif;
  font-weight: bold;
  color: white;
}

.home-container {
  background-size: cover;
  background-position: center;
  display: grid;
  place-items: center;
  
}

.home-card {
  padding: 50px;
  text-align: center;
  background-color: rgb(255, 255, 255);
  border-radius: 10px;
  width: 100%;
  margin-top: 50px;
  display: flex;
  align-items: center;
  flex-direction: column;;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

.close-button {
  position: absolute;
  top: 90px;
  right: 180px;
  cursor: pointer;
  background: none;
  border: none;
  font-size: 16px;
  color: #ff0000;
  z-index: 1;
}

.login-slider {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 132, 255, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999;
}
</style>
