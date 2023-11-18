<template>
    <div class="container">
        <h1>ACTIVITIES</h1>
        <div class="slider-container">
            <div class="slider">
                <div v-if="resources.length > 0" class="resource-card" :style="resourceCardStyle">
                    <div class="resource-content">
                        <div class="resource-data">
                            <p>Goal: {{ resources[currentIndex].goal }}</p>
                            <p>Level: {{ resources[currentIndex].lvl }}</p>
                            <p>PT: {{ resources[currentIndex].pt }}</p>
                           
                        </div>
                        <div class="resource-media">
                            <div v-if="resources[currentIndex].url === 'PrepositionOfTimeIllustrationlow'">
                                <img src="../../learning_resources/timeilustrationlow.png" alt="imagen" style="max-height: 100%;">
                                <!-- <vue-pdf-embed :source="fileSource" /> -->
                                
                               
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfTimesimulationslow'" class="h5p-container">
                                <iframe src="https://h5p.org/h5p/embed/1442390" width="1088" height="983" frameborder="0"
allowfullscreen="allowfullscreen" allow="geolocation *; microphone *; camera *; midi *;
encrypted-media *" title="PREPOSITIONS OF TIME" ></iframe>

                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfTimequestions_and_answerslow'" class="h5p-container" >
                                <iframe src="https://h5p.org/h5p/embed/1444597" width="1090" height="337" frameborder="0"
allowfullscreen="allowfullscreen" allow="geolocation *; microphone *; camera *; midi *;
encrypted-media *" title="PREPOSITIONS OF TIME QN1"></iframe>

                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfTimelecturelow'">
                                <img src="../../learning_resources/timelecturelow_page-0001.jpg" alt="imagen" style="max-height: 100%;">
                            </div>    
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfTimeIllustrationmedium'">
                                <img src="../../learning_resources/timeilustrationmedium.png" alt="imagen" style="max-height: 100%;">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfTimesimulationsmedium'" class="h5p-container">
                                <iframe src="https://h5p.org/h5p/embed/1442486" width="1088" height="707" frameborder="0"
allowfullscreen="allowfullscreen" allow="geolocation *; microphone *; camera *; midi *;
encrypted-media *" title="PREPOSITIONS OF TIME N1"></iframe>                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfTimequestions_and_answersmedium'" class="h5p-container">
                                <iframe src="https://h5p.org/h5p/embed/1444630" width="1090" height="337" frameborder="0"
allowfullscreen="allowfullscreen" allow="geolocation *; microphone *; camera *; midi *;
encrypted-media *" title="PREPOSITIONS OF TIME QN2"></iframe>
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfTimelecturemedium'">
                                <img src="../../learning_resources/timelecturemedium_page-0001.jpg" alt="imagen" style="max-height: 100%;">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfTimeIllustrationhigh'">
                                <img src="../../learning_resources/timeilustrationhigh.png" alt="imagen" style="max-height: 100%;">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfTimesimulationshigh'" class="h5p-container">
                                <iframe src="https://h5p.org/h5p/embed/1442430" width="1088" height="475" frameborder="0"
allowfullscreen="allowfullscreen" allow="geolocation *; microphone *; camera *; midi *;
encrypted-media *" title="PREPOSITIONS OF TIME N3"></iframe>                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfTimequestions_and_answershigh'" class="h5p-container">
                                <iframe src="https://h5p.org/h5p/embed/1444607" width="1090" height="463" frameborder="0"
allowfullscreen="allowfullscreen" allow="geolocation *; microphone *; camera *; midi *;
encrypted-media *" title="PREPOSITIONS OF TIME QN3"></iframe>                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfTimelecturehigh'">
                                <img src="../../learning_resources/timelecturehigh_page-0001.jpg" alt="imagen" style="max-height: 100%;">
                               
                            </div>
                            <div v-else-if="resources[currentIndex].url === 'PrepositionOfPlaceIllustrationlow'">
                                <img src="../../learning_resources/placeilustrationlow.png" alt="imagen" style="max-height: 100%;">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfPlacesimulationslow'" class="h5p-container">
                                <iframe src="https://h5p.org/h5p/embed/1456138" width="1091" height="892" frameborder="0" allowfullscreen="allowfullscreen" allow="geolocation *; microphone *; camera *; midi *; encrypted-media *" title="PREPOSITIONS OF PLACE S1"></iframe>                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfPlacequestions_and_answerslow'" class="h5p-containerr">
                                <iframe src="https://h5p.org/h5p/embed/1456116" width="1091" height="803" frameborder="0" allowfullscreen="allowfullscreen" allow="geolocation *; microphone *; camera *; midi *; encrypted-media *" title="PREPOSITIONS OF PLACE 1"></iframe>                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfPlacelecturelow'">
                                <img src="../../learning_resources/placelecturelow_page-0001.jpg" alt="imagen" style="max-height: 100%;">
                                
                            </div>    
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfPlaceIllustrationmedium'">
                                <img src="../../learning_resources/placeilustrationmeium.png" alt="imagen" style="max-height: 100%;">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfPlacesimulationsmedium'" class="h5p-container">
                                <iframe src="https://h5p.org/h5p/embed/1456151" width="1086" height="976" frameborder="0"
allowfullscreen="allowfullscreen" allow="geolocation *; microphone *; camera *; midi *;
encrypted-media *" title="PREPOSITIONS OF PLACE S2"> </iframe>                         </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfPlacequestions_and_answersmedium'" class="h5p-container">
                                <iframe src="https://h5p.org/h5p/embed/1456175" width="1090" height="336" frameborder="0"
allowfullscreen="allowfullscreen" allow="geolocation *; microphone *; camera *; midi *;
encrypted-media *" title="PREPOSITIONS OF PLACE Q2"></iframe>                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfPlacelecturemedium'">
                                <img src="../../learning_resources/placelecturemedium.png" alt="imagen" style="max-height: 100%;">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfPlaceIllustrationhigh'">
                                <img src="../../learning_resources/placeilustrationhigh.png" alt="imagen" style="max-height: 100%;">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfPlacesimulationshigh'">
                                <iframe src="https://myh5unicor.h5p.com/content/1292105884748311508/embed" aria-label="simulacion p.place nivel alto" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfPlacequestions_and_answershigh'">
                                <iframe src="https://myh5unicor.h5p.com/content/1292105876612306768/embed" aria-label="preposition place nivel 3" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                                <iframe src="https://myh5unicor.h5p.com/content/1292105873975063138/embed" aria-label="preposition place nivel 3" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                                <iframe src="https://myh5unicor.h5p.com/content/1292105869842271398/embed" aria-label="preposition place nivel 3" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfPlacelecturehigh'">
                                <img src="../../learning_resources/placelecturehigh.png" alt="imagen" style="max-height: 100%;">                            </div>
                            <div v-else-if="resources[currentIndex].url === 'PrepositionOfMovementIllustrationlow'">
                                <img src="../../learning_resources/movementIllustrationlow.png" alt="imagen" style="max-height: 100%;">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfMovementsimulationslow'">
                                <iframe src="https://myh5unicor.h5p.com/content/1292105766833396308/embed" aria-label="Preposition movement nivel 1" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfMovementquestions_and_answerslow'">
                                <iframe src="https://myh5unicor.h5p.com/content/1292082396756922898/embed" aria-label="preposition of movement- Level 1" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                                <iframe src="https://myh5unicor.h5p.com/content/1292082397924278848/embed" aria-label="preposition of movement- Level 1" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                                <iframe src="https://myh5unicor.h5p.com/content/1292082395969161128/embed" aria-label="preposition of movement- Level 1" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfMovementlecturelow'">
                                <img src="../../learning_resources/movementlecturelow.png" alt="imagen" style="max-height: 100%;"> 
                            </div>    
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfMovementIllustrationmedium'">
                                <img src="../../learning_resources/movementIllustrationmedium.png" alt="imagen" style="max-height: 100%;"> 
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfMovementsimulationsmedium'">
                                <iframe src="https://myh5unicor.h5p.com/content/1292105778719434208/embed" aria-label="Preposition movement nivel 2" width="1088" height="637"
 frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfMovementquestions_and_answersmedium'">
                            <iframe src="https://myh5unicor.h5p.com/content/1292082403067734278/embed" aria-label="preposition of movement- Level 2" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                            <iframe src="https://myh5unicor.h5p.com/content/1292082401585524158/embed" aria-label="preposition of movement- Level 2" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                            <iframe src="https://myh5unicor.h5p.com/content/1292082402398392048/embed" aria-label="preposition of movement- Level 2" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfMovementlecturemedium'">
                                <img src="../../learning_resources/movementlecturemedium.png" alt="imagen" style="max-height: 100%;">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfMovementIllustrationhigh'">
                                <img src="../../learning_resources/movementilustrationhigh.png" alt="imagen" style="max-height: 100%;">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfMovementsimulationshigh'">
                                <iframe src="https://myh5unicor.h5p.com/content/1292105788178762388/embed" aria-label="Preposition movement nivel 3" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfMovementquestions_and_answershigh'">
                                <iframe src="https://myh5unicor.h5p.com/content/1292082404691150338/embed" aria-label="preposition of movement- Level 3" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                                <iframe src="https://myh5unicor.h5p.com/content/1292082403716188728/embed" aria-label="preposition of movement- Level 3" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                                <iframe src="https://myh5unicor.h5p.com/content/1292082406126423008/embed" aria-label="preposition of movement- Level 3" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>                            
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'PrepositionOfMovementlecturehigh'">
                                <img src="../../learning_resources/movementlecturehigh.png" style="max-height: 100%;">
                            </div>                                                                                        
                            <div v-else>
                                <p>No hay recursos para mostrar</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="buttons">
                <button class="prev-button" @click="prevSlide">Anterior</button>
                <button class="next-button" @click="nextSlide">Siguiente</button>
            </div>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios';
// import VuePdfEmbed from 'vue-pdf-embed'
// import VueH5P from 'vue-h5p';

export default {
    components: {
        // VuePdfEmbed
    },
    data() {
        return {
            resources: [],
            additionalResources: [],
            currentIndex: 0,
            fileSource: require('!file-loader!../../learning_resources/placelecturelow.pdf'),
            h5pOptions: {
            content: './h5p/prepositions-of-time-24-1445976.h5p', // Reemplaza con la ruta correcta a tu archivo H5P
    },
        };
    },

    
    computed: {
    resourceCardStyle() {
      return {
        width: '100%',
        display: this.resources.length > 0 ? 'flex' : 'none'
      };
    }
  },

    mounted() {
        this.axiosCallSequential();
        this.movementquestions_and_answershigh()
    },
    methods: {
        axiosCallSequential() {
                const id_student = this.$store.state.userId
                axios.get(`/api/Activity/${id_student}`) 
                .then(response => {
                    this.resources = response.data.resource_list;
                    this.additionalResources = response.data.resource_list_additional
                    console.log('additional', this.resources)
                })
                .catch(error => {
                    console.log(error, 'Error al capturar');
                });
        },

//         movementquestions_and_answershigh() {
//             const h5pContainer = this.$refs.h5pContainer; // Asegúrate de tener un ref en tu plantilla HTML
//             const h5pParams = {
//     // Configuración de tu actividad H5P (puede variar según la actividad)
//             content: '../../../public/h5p/preposition-of-movement-level-3-1292082403716188728.h5p', // Ruta al contenido H5P
//             // frameJs: 'path_to_h5p_frame_bundle.js', // Ruta al bundle de H5P
//             // frameCss: 'path_to_h5p_frame_bundle.css', // Ruta al CSS de H5P
//             displayOptions: {
//       // Opciones de visualización (pueden variar según tus necesidades)
//             frame: true,
//         },
//   };

//         const h5p = new H5PStandalone.H5P(h5pParams, h5pContainer)
//         console.log(h5p)
//         },

//         movementsimulationshigh() {
//             const h5pContainer = this.$refs.h5pContainer; // Asegúrate de tener un ref en tu plantilla HTML
//             const h5pParams = {
//     // Configuración de tu actividad H5P (puede variar según la actividad)
//             content: '../../../public/h5p/preposition-of-movement-level-3-1292082403716188728.h5p', // Ruta al contenido H5P
//             // frameJs: 'path_to_h5p_frame_bundle.js', // Ruta al bundle de H5P
//             // frameCss: 'path_to_h5p_frame_bundle.css', // Ruta al CSS de H5P
//             displayOptions: {
//       // Opciones de visualización (pueden variar según tus necesidades)
//             frame: true,
//         },
//   };

//         const h5p = new H5PStandalone.H5P(h5pParams, h5pContainer)
//         console.log(h5p)
//         },


        prevSlide() {
            if (this.currentIndex > 0) {
                this.currentIndex--;
            }
        },
        nextSlide() {
            if (this.currentIndex < this.resources.length - 1) {
                this.currentIndex++;
            }
        }
    }
};
</script>
  

<style>

.container { 
  background-color: white;
  border-radius: 0 0 20px 20px;

}

.container h1 { 
  font-family: 'Roboto' sans-serif;
  font-weight: bold;
  color: #0099ff;
}

.slider-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;   
}

.resource-card {
  display: none;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  border-radius: 20px 20px 0 0;
  
}

.resource-card.active {
  display: flex;
}
.h5p-container {
  width: 1000px; /* Ancho deseado */
  height: 100%; /* Alto deseado */
}

.h5p-containerr {
  width: 350px; /* Ancho deseado */
  height: 100%; /* Alto deseado */
}

@media (max-width: 1200px) {
  /* .resource-content {
  } */

  .h5p-container {
    width: 400px; /* Ancho deseado */
  height: 100%;  }
}

.resource-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

}


.resource-media {
  margin-top: 20px;
}

.resource-media img,
.resource-media video,
.resource-media iframe {
  max-width: 100%;
  max-height: 70vh;
}
.buttons {
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 10px;
}

.prev-button,
.next-button {
  background-color:rgb(36, 149, 255);
  color: white;
  border: none;
  border-radius: 4px;
  padding: 10px 20px;
  margin: 0 10px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.buttons {
    max-height: 100vh;
}

.prev-button:hover,
.next-button:hover {
  background-color: #0078c9;
  transform: scale(1.1);
}


.resource-data h2,
.resource-data p {
  margin: 0;
}

.resource-data {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: row !important;
}
</style>