<template>
  <v-container>
      <v-row align="center" justify="center" >
          <v-col cols="12" sm="10">
            <v-card class="elevation-6 mt-10"  >
             <v-window v-model="step">
                <v-window-item :value="1">
                  <v-row>
                    <v-col cols="12" md="6">
                      <v-card-text class="mt-12">
                        <h4
                          class="text-center"
                        >Login in to Your Account</h4>
                        <h5
                          class="text-center  grey--text "
                        >Log in to your account so you can continue</h5>
                        <v-row align="center" justify="center">
                          <v-col cols="12" sm="8">
                           
                          <v-text-field
                            v-model="user"
                            label="Username"
                            outlined
                            dense
                            color="blue"
                            autocomplete="false"
                           class="mt-16"
                          />
                          <v-text-field
                            v-model="password"
                            label="Password"
                            outlined
                            dense
                            color="blue"
                          autocomplete="false"
                           type="password"
                          
                          />
                            <v-row>
                              <v-col cols="12" sm="7">
                                <span class="caption blue--text">Forgot password</span>
                              </v-col>

                            </v-row>
                            <br>
                          <v-btn color="blue" dark block tile @click="onSubmit">Log in</v-btn>
            
                          </v-col>
                        </v-row>  
                      </v-card-text>
                    </v-col>
                    <v-col cols="12" md="6" class="blue rounded-bl-xl" >
                    <div style="  text-align: center; padding: 180px 0;">
                      <v-card-text class="white--text" >
                        <h3 class="text-center ">Don't Have an Account Yet?</h3>
                        <h5
                          class="text-center"
                        >Let's register to log in</h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn tile outlined dark @click="step++">SIGN UP</v-btn>
                      </div>
                      </div>
                    </v-col>
                  </v-row>
                </v-window-item>
                <v-window-item :value="2">
                  <v-row >
                    <v-col cols="12" md="6" class="blue rounded-br-xl">
                     <div style="  text-align: center; padding: 180px 0;">
                      <v-card-text class="white--text" >
                        <h3 class="text-center ">Alredy Signed up?</h3>
                        <h5
                          class="text-center"
                        >Log in to your account so you can continue</h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn tile outlined dark @click="step--">Log in</v-btn>
                      </div>
                      </div>
                    </v-col>

                    <v-col cols="12" md="6">
                      <v-card-text class="mt-12">
                        <h4
                          class="text-center"
                        >Sign Up for an Account</h4>
                        <h5
                          class="text-center  grey--text "
                        >Let's register to log in</h5>
                        <br>
                        <v-row align="center" justify="center">
                          <v-col cols="12" sm="8">

                              <v-file-input v-model="picture" label="Agregue una foto" accept="image/*" required></v-file-input>
                     
                            <v-text-field
                            v-model="name"
                            label="Full Name"
                            outlined
                            dense
                            color="blue"
                            autocomplete="false"
                           class="mt-4"
                          />

                          <v-text-field
                            v-model="userRegistered"
                            label="Email"
                            outlined
                            dense
                            color="blue"
                            autocomplete="false"
                          />
                          <v-text-field
                            v-model="passwordRegistered"
                            label="Password"
                            outlined
                            dense
                            color="blue"
                          autocomplete="false"
                           type="password"
                          
                          />
                          <v-btn color="blue" dark block tile @click="register">Sign up</v-btn>
                    
                          </v-col>
                        </v-row>  
                      </v-card-text>
                    </v-col>
                  </v-row>
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
                </v-window-item>
              </v-window>
            </v-card>
          </v-col>
      </v-row>
  </v-container>
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
.v-application .rounded-bl-xl {
    border-bottom-left-radius: 300px !important;
}
.v-application .rounded-br-xl {
    border-bottom-right-radius: 300px !important;
}
</style>