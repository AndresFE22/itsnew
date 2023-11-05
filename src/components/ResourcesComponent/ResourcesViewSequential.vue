<template>
    <div class="container">
        <h1>ACTIVITIES</h1>
        <div class="slider-container">
            <div class="slider">
                <div v-if="resources.length > 0" class="resource-card" :style="resourceCardStyle">
                    <div class="resource-content">
                        <div class="resource-data">
                            <h2>{{ resources[currentIndex].name }}</h2>
                            <p>Goal: {{ resources[currentIndex].goal }}</p>
                            <p>Level: {{ resources[currentIndex].lvl }}</p>
                            <p>PT: {{ resources[currentIndex].pt }}</p>
                        </div>
                        <div class="resource-media">
                            <div v-if="resources[currentIndex].url === 'timeIllustrationlow'">
                                <img src="../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'timesimulationslow'">
                                <img src="../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'timequestions_and_answerslow'">
                                <img src="../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'timelecturelowg'">
                                <iframe src="../../learning_resources/t1.txt" frameborder="0"></iframe>
                            </div>    
                            <div v-else-if="resources[currentIndex].url == 't1Illustrationmedium'">
                                <img src="../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'timesimulationsmedium'">
                                <img src="../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'timequestions_and_answersmedium'">
                                <img src="../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'timelecturemedium'">
                                <iframe src="../../learning_resources/t1.txt" frameborder="0"></iframe>
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'timeIllustrationhigh'">
                                <img src="../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'timesimulationshigh'">
                                <img src="../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'timequestions_and_answershigh'">
                                <img src="../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'timelecturehigh'">
                                <iframe src="../../learning_resources/t1.txt" frameborder="0"></iframe>
                            </div>
                            <div v-else-if="resources[currentIndex].url === 'placeIllustrationlow'">
                                <img src="../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'placesimulationslow'">
                                <img src="../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'placequestions_and_answerslow'">
                                <img src="../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'placelecturelowg'">
                                <iframe src="../../learning_resources/t1.txt" frameborder="0"></iframe>
                            </div>    
                            <div v-else-if="resources[currentIndex].url == 'placeIllustrationmedium'">
                                <img src="../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'placesimulationsmedium'">
                                <img src="../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'placequestions_and_answersmedium'">
                                <img src="../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'placelecturemedium'">
                                <iframe src="../../learning_resources/t1.txt" frameborder="0"></iframe>
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'placeIllustrationhigh'">
                                <img src="../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'placesimulationshigh'">
                                <img src="../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'placequestions_and_answershigh'">
                                <img src="../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'placelecturehigh'">
                                <iframe src="../../learning_resources/t1.txt" frameborder="0"></iframe>
                            </div>
                            <div v-else-if="resources[currentIndex].url === 'movementIllustrationlow'">
                                <img src="../../learning_resources/movementIllustrationlow.png" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'movementsimulationslow'">
                                <iframe src="https://myh5unicor.h5p.com/content/1292105766833396308/embed" aria-label="Preposition movement nivel 1" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'movementquestions_and_answerslow'">
                                <iframe src="https://myh5unicor.h5p.com/content/1292082396756922898/embed" aria-label="preposition of movement- Level 1" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                                <iframe src="https://myh5unicor.h5p.com/content/1292082397924278848/embed" aria-label="preposition of movement- Level 1" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                                <iframe src="https://myh5unicor.h5p.com/content/1292082395969161128/embed" aria-label="preposition of movement- Level 1" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'movementlecturelow'">
                                <iframe src="../../learning_resources/movementlecturelow.png" frameborder="0"></iframe>
                            </div>    
                            <div v-else-if="resources[currentIndex].url == 'movementIllustrationmedium'">
                                <img src="../../learning_resources/movementIllustrationmedium.png" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'movementsimulationsmedium'">
                                <iframe src="https://myh5unicor.h5p.com/content/1292105778719434208/embed" aria-label="Preposition movement nivel 2" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'movementquestions_and_answersmedium'">
                            <iframe src="https://myh5unicor.h5p.com/content/1292082403067734278/embed" aria-label="preposition of movement- Level 2" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                            <iframe src="https://myh5unicor.h5p.com/content/1292082401585524158/embed" aria-label="preposition of movement- Level 2" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                            <iframe src="https://myh5unicor.h5p.com/content/1292082402398392048/embed" aria-label="preposition of movement- Level 2" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'movementlecturemedium'">
                                <iframe src="../../learning_resources/movementlecturemedium.png" frameborder="0"></iframe>
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'movementIllustrationhigh'">
                                <img src="../../learning_resources/movementilustrationhigh.png" alt="imagen">
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'movementsimulationshigh'">
                                <iframe src="https://myh5unicor.h5p.com/content/1292105788178762388/embed" aria-label="Preposition movement nivel 3" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                            </div>
                            <div v-else-if="resources[currentIndex].url == 'movementquestions_and_answershigh'">
                                <iframe src="https://myh5unicor.h5p.com/content/1292082404691150338/embed" aria-label="preposition of movement- Level 3" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                                <iframe src="https://myh5unicor.h5p.com/content/1292082403716188728/embed" aria-label="preposition of movement- Level 3" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                                <iframe src="https://myh5unicor.h5p.com/content/1292082406126423008/embed" aria-label="preposition of movement- Level 3" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>                            
                            </div>
                            <div v-else-if="resources[currentIndex].url == 't1Illustrationlow'">
                                <img src="../../learning_resources/movementlecturehigh.png">
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


export default {
    data() {
        return {
            resources: [],
            additionalResources: [],
            currentIndex: 0
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
                    console.log('additional', this.additionalResources)
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

.prev-button:hover,
.next-button:hover {
  background-color: #0078c9;
  transform: scale(1.1);
}


.resource-data h2,
.resource-data p {
  margin: 0;
}
</style>