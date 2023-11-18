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
                        <span style="cursor: pointer;" class="text-primary" @click="step = 3">Forgot password</span>
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
                    <input v-model="userRegistered" type="text" class="form-control mt-3" placeholder="Username">
                    <input v-model="passwordRegistered" type="password" class="form-control mt-3" placeholder="Password">
                    <v-file-input v-model="picture" label="Add a photo" accept="image/*" required></v-file-input>
                    <button @click="register" class="btn btn-primary btn-block mt-4">Sign up</button>
                  </div>
                </div>
              </div>
            </div>

            <div v-else-if="step === 3">
              <div class="card-body">
                <h4 class="text-center">Change of password</h4>
                <h5 class="text-center text-secondary">Let's register to log in</h5>
                <div class="row justify-content-center">
                  <div class="col-md-8 mt-4">
                    <input v-model="usernameVerified" type="text" class="form-control mt-3" placeholder="Username">
                    <input v-model="newPassword" type="password" class="form-control mt-3" placeholder="New password">
                    <button @click="change" class="btn btn-primary btn-block mt-4">Change Password</button>
                  </div>
                </div>
              </div>
            </div>

            <div class="row justify-content-center mt-3">
          <div class="text col-md-8 text-center">
            <div v-if="step === 1">
              <span class="text-primary"  @click="step = 2">Don't Have an Account Yet? Sign Up</span>
            </div>
            <div v-else-if="step === 2 || 3">
              <span class="text-primary" @click="step = 1">Already Signed up? Log in</span>
            </div>
          </div>
        </div>
        <transition name="fade">
          <div v-if="message === 'User registered successfully'" class="msg">
            <div class="msgtext">
             <h4>
              {{ message }}
            </h4>
            </div>
          </div>
        </transition>
        <transition name="fade">
          <div v-if="message === 'The user is already registered'" class="msge">
            <div class="msgtexte">
             <h4>
              {{ message }}
            </h4>
            </div>
          </div>
        </transition>
        <transition name="fade">
          <div v-if="message === 'Login failed'" class="msge">
            <div class="msgtexte">
             <h4>
              {{ message }}
            </h4>
            </div>
          </div>
        </transition>
        <transition name="fade">
          <div v-if="message === 'Password updated successfully'" class="msg">
            <div class="msgtext">
             <h4>
              {{ message }}
            </h4>
            </div>
          </div>
        </transition>
        <transition name="fade">
          <div v-if="message === 'User not found'" class="msge">
            <div class="msgtexte">
             <h4>
              {{ message }}
            </h4>
            </div>
          </div>
        </transition>
          </div>
          
       
          <b-modal v-if="errorModal" title="Error al iniciar sesión">
  <p>{{ errorAuth }}</p>
  <button @click="error = false">Cerrar</button>
      </b-modal>
        </transition>
      </div>
       
      </div>
    </div>
</template>

<script>

import axios from 'axios'
// import forgotPassword from './forgotPassword.vue'
  
  export default {
    // components: {
    //   forgotPassword
    // },
    data() {
  return {
    step: 1,
    user: '',
    password: '',
    name: '',
    userRegistered: '',
    passwordRegistered: '',
    message: '',
    messageLogin: null,
    error: '',
    errorAuth: null,
    errorModal: false,
    picture: null,
    usernameVerified: null,
    newPassword: null
  }
},

  props: {
    source: String
  }, 
  methods: {
    async onSubmit() {
  axios
    .post('/api/login', {
      user: this.user,
      password: this.password
    })
    .then((response) => {
      this.message = response.data.message;
      setTimeout(() => {
          this.message = '';
        }, 2000);

      console.log(response.data.message);
      console.log(response.data.user.id);

      if (response.data.message === 'Login successful') {
        localStorage.setItem('isLoggedIn', 'true');
        const userId = response.data.user.id;
        const userData = response.data.user;
        this.$store.commit('setUserId', userId);
        this.$store.commit('setUserData', userData);
        localStorage.setItem('userId', userId);

        this.$store.dispatch('doLogin', this.user).then(() => {
          axios.get(`/api/stateVerified/${userId}`).then((estadoResponse) => {
            const estadoData = estadoResponse.data;
            console.log(estadoData);

            if (estadoData.TestStyle === 0 || estadoData.TestStyle === null) {
              this.$router.push({ name: 'DiagnosisStyles' });
            } else if (
              estadoData.TestTopic === 0 ||
              estadoData.TestTopic === null
            ) {
              this.$router.push({ name: 'DiagnosisState' });
            } else if (
              estadoData.GoalCompleted === 1
            ) {
              this.$router.push({ name: 'DiagnosisState' });
            }
            else {
              this.$router.push({ name: 'ActivityITS' });
            }
          });
        });
      } else {
        console.log(response.data.message);
        this.message = response.data.message;
      }
    })
    .catch((error) => {
      console.error(error);
    });
},

change() {
        axios
          .put("/api/changePassword", {
            user: this.usernameVerified,
            newPassword: this.newPassword,
          })
          .then((response) => {
            this.message = response.data.message;
            setTimeout(() => {
          this.message = '';
        }, 2000);
            console.log(response.data.message);
            if ( response.data.message === 'Password updated successfully') {
              this.message = response.data.message;
            setTimeout(() => {
          this.message = '';
          this.userRegistered = '';
          this.newPassword = ''
        }, 2000);
            } 
           
          })
          .catch((error) => {
            console.error(error);
          });
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

.msg {
    position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 211, 46, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999;

  }

  .msgtext {
    background-color: white;
    color: rgba(0, 211, 46, 0.7);
    font-weight: bold;
    border-radius: 20px;
    display: grid;
    place-items: center;
    padding: 20px;


  }

  .msge {
    position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(211, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999;

  }

  .msgtexte {
    background-color: white;
    color: rgba(211, 0, 0, 0.7);
    font-weight: bold;
    border-radius: 20px;
    display: grid;
    place-items: center;
    padding: 20px;


  }

</style>