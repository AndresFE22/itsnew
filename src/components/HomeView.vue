<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-10">
        <transition name="transition" mode="out-in">
          <div class="card mt-10" :key="step">
            <div v-if="step === 1">
              <div class="card-body">
                <h4 class="text-center">Login in to Your Account</h4>
                <h5 class="text-center text-secondary">Log in to your account so you can continue</h5>
                <div class="row justify-content-center">
                  <div class="col-md-8 mt-4">
                    <input v-model="user" type="text" class="form-control" placeholder="Username">
                    <input v-model="password" type="password" class="form-control mt-3" placeholder="Password">
                    <div class="row mt-3">
                      <div class="col-md-4">
                        <span class="text-primary">Forgot password</span>
                      </div>
                    </div>
                    <button @click="onSubmit" class="btn btn-primary btn-block mt-4">Log in</button>
                  </div>
                </div>
              </div>
            </div>

            <div v-else-if="step === 2">
              <div class="card-body">
                <h4 class="text-center">Sign Up for an Account</h4>
                <h5 class="text-center text-secondary">Let's register to log in</h5>
                <div class="row justify-content-center">
                  <div class="col-md-8 mt-4">
                    <input v-model="name" type="text" class="form-control" placeholder="Full Name">
                    <input v-model="userRegistered" type="text" class="form-control mt-3" placeholder="Email">
                    <input v-model="passwordRegistered" type="password" class="form-control mt-3" placeholder="Password">
                    <v-file-input v-model="picture" label="Agregue una foto" accept="image/*" required></v-file-input>
                    <button @click="register" class="btn btn-primary btn-block mt-4">Sign up</button>
                  </div>
                </div>
              </div>
            </div>
            <div class="row justify-content-center mt-3">
          <div class="text col-md-8 text-center">
            <div v-if="step === 1">
              <span class="text-primary"  @click="step = 2">Don't Have an Account Yet? Sign Up</span>
            </div>
            <div v-else-if="step === 2">
              <span class="text-primary" @click="step = 1">Already Signed up? Log in</span>
            </div>
          </div>
        </div>
          </div>
        </transition>
      </div>
       
      </div>
    </div>
</template>

<script>

import axios from 'axios'
  
  export default {
    data() {
  return {
    step: 1,
    user: '',
    password: '',
    name: '',
    userRegistered: '',
    passwordRegistered: '',
    message: '',
    error: '',
    picture: null
  }
},

  props: {
    source: String
  }, 
  methods: {
    async onSubmit() {
  try {
    const response = await axios.post('/api/login', {
      user: this.user,
      password: this.password
    });

    console.log(response.data.message);
    console.log(response.data.user.id);
    if (response.data.message === 'Login successful') {
      localStorage.setItem('isLoggedIn', 'true')
      const userId = response.data.user.id
      const userData = response.data.user
      this.$store.commit('setUserId', userId)
      this.$store.commit('setUserData', userData)
      localStorage.setItem('userId', userId)
      await this.$store.dispatch('doLogin', this.user);

      const estadoResponse = await axios.get(`/api/stateVerified/${userId}`);
      const estadoData = estadoResponse.data;
      console.log(estadoData);

      if (estadoData.TestTopic === 0 || estadoData.TestTopic === null) {
        this.$router.push({ name: 'DiagnosisState' });
      } else if (estadoData.TestStyle === 0 || estadoData.TestStyle === null) {
        this.$router.push({ name: 'DiagnosisStyles' });
      } else {
        this.$router.push({ name: 'ActivityITS' });
      }
    }
  } catch (error) {
    console.error(error);
  }
},

  checkAuthStatus() {
      console.log('Estado de autenticación:', this.auth);
    },
    register() {
      const formData = new FormData();
      formData.append('name', this.name)
      formData.append('user', this.userRegistered) 
      formData.append('password', this.passwordRegistered) 
      formData.append('picture', this.picture) 

      axios.post('api/register', formData)
      .then(response => {
        this.message = response.data.message;
        setTimeout(() => {
          this.message= "";
        }, 2000 
        )
        if (this.message === 'User registered successfully') {
          this.name= "",
          this.userRegistered="",
          this.passwordRegistered=""
          this.picture=null
        }
        console.log(response.data.message);
      })
      .catch(error => {
        console.error(error);
      });
    },
    closeMessage() {
      this.message = '';
      this.error = '';

    }
},

    
  }
</script>
<style scoped>
.transition-enter-active, .transition-leave-active {
  transition: transform 0.5s, opacity 0.5s; /* Se combinan las transiciones */
}

.transition-enter, .transition-leave-to {
  transform: translateX(-30%);
  opacity: 0;
}

.transition-enter-to, .transition-leave {
  transform: translateX(0%);
  opacity: 1;
}

.card {
  max-width: 100%; /* Establece el ancho máximo a 100% del contenedor padre */
}

.text{
  margin-bottom: 30px;
  text-decoration: underline;
  color: rgb(0, 174, 255);
  cursor: pointer;
}

</style>