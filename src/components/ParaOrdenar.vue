<template>
    <div>
      <h1>Organizador de historias</h1>
  
      <div v-for="(name, index) in names" :key="index">
        <select v-model="orderedNames[index]" style="width: 30%; border: 1px solid black;">
          <option v-for="(name, i) in names" :key="i">{{ name }}</option>
        </select>
      </div>
  
      <button @click="organizarNombres">Organizar</button>
  
      <div v-if="resultado.length > 0">
        <h2>Resultado Organizado:</h2>
        <ul>
          <li v-for="(name, index) in resultado" :key="index">{{ name }}</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  export default {
    data() {
      return {
        names: ["PrepositionOfTimeLow1", "PrepositionOfTimeMedium2", "PrepositionOfTimeHigh3", "PrepositionOfPlaceLow4", "PrepositionOfPlaceMedium5", "PrepositionOfPlaceHigh6", "PrepositionOfMovementLow7", "PrepositionOfMovementMedium8", "PrepositionOfMovementHigh9"],
        orderedNames: [],
        resultado: [],
      };
    },
  
    methods: {
      organizarNombres() {
        // Mostrar el resultado
        this.resultado = this.orderedNames;
        const resultado = this.resultado
        const id = 2
          console.log('resultado', resultado)
          axios.post(`/api/ordenar/${id}`, { resultado : resultado})
          .then(response => {
              console.log(response.data);
          })
          .catch(error => {
              console.log(error, 'Error al enviar')
          }) 

      },
    },
  };
  </script>
  