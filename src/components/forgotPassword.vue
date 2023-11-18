<template>
    <div class="modal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <h2>Cambio de Contraseña</h2>
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="username">Usuario:</label>
            <input type="text" v-model="username" required />
          </div>
          <div class="form-group">
            <label for="newPassword">Nueva Contraseña:</label>
            <input type="password" v-model="newPassword" required />
          </div>
          <div class="form-group">
            <button type="submit">Cambiar Contraseña</button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: "",
        newPassword: "",
      };
    },
    methods: {
      closeModal() {
        // Lógica para cerrar el modal
      },
      submitForm() {
        // Lógica para enviar los datos al servidor usando Axios
        this.$axios
          .put("api/changepassword", {
            user: this.username,
            newPassword: this.newPassword,
          })
          .then((response) => {
            // Manejar la respuesta del servidor según sea necesario
            console.log(response.data);
            this.closeModal();
          })
          .catch((error) => {
            // Manejar los errores
            console.error(error);
          });
      },
    },
  };
  </script>
  
  <style scoped>
  /* Estilos para el modal, ajusta según sea necesario */
  .modal {
    display: none;
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.4);
  }
  
  .modal-content {
    background-color: #fefefe;
    margin: 15% auto;
    padding: 20px;
    border: 1px solid #888;
    width: 80%;
  }
  
  .close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
  }
  
  .close:hover,
  .close:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  </style>
  