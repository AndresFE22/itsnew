<template>
  <div class="register-container">
    <div class="register-card">
      <h1 class="register-title">Register</h1>
      <form class="register-form">
        <div class="form-group">
          <v-file-input v-model="picture" label="Agregue una foto" accept="image/*" required></v-file-input>
          <input v-model="name" id="name" class="form-control" placeholder="Enter your fullname" />
        </div>
        <div class="form-group">
          <input v-model="user" id="username" class="form-control" placeholder="Enter your username" />
        </div>
        <div class="form-group">
          <input v-model="password" id="password" class="form-control" type="password" placeholder="Enter your password" />
        </div>
        <button @click="register" class="register-button">register</button>
      </form>
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
      </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      user: '',
      password: '',
      message: '',
      error: '',
      picture: null
    };
  },
  methods: {
    register() {
      const formData = new FormData();
      formData.append('name', this.name)
      formData.append('user', this.user) 
      formData.append('password', this.password) 
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
          this.user="",
          this.password=""
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
  }
};
</script>

<style scoped>


.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 45vh;
}

.register-card {
  background-color: #ffffff;
  border-radius: 10px;
  padding: 30px;
  width: 100%;
  max-width: 500px;
  height: 350px;
  overflow: hidden; /* o scroll, hidden, etc., según tus necesidades */
  
}

.register-title {
  font-size: 24px;
  margin-bottom: 20px;
}

.register-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

.form-control {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

.register-button {
  background-color: #0084ff;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.register-button:hover {
  background-color: #0064cc;
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
