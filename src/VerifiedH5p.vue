<template>
    <div class="container">
        <iframe src="https://myh5unicor.h5p.com/content/1292082403067734278/embed" aria-label="preposition of movement- Level 2" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                            <iframe src="https://myh5unicor.h5p.com/content/1292082401585524158/embed" aria-label="preposition of movement- Level 2" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
                            <iframe src="https://myh5unicor.h5p.com/content/1292082402398392048/embed" aria-label="preposition of movement- Level 2" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe>
    </div>
</template>
  
<script>
import H5PStandalone from 'h5p-standalone';


export default {
    data() {
        return {
            resources: [],
            additionalResources: [],
            currentIndex: 0
        };
    },

    mounted() {
        this.movementquestions_and_answershigh()
    },
    methods: {

        movementquestions_and_answershigh() {
            const h5pContainer = this.$refs.h5pContainer; // Asegúrate de tener un ref en tu plantilla HTML
            const h5pParams = {
    // Configuración de tu actividad H5P (puede variar según la actividad)
            content: './h5p/preposition-of-movement-level-3-1292082403716188728.h5p',
            // frameJs: 'path_to_h5p_frame_bundle.js', // Ruta al bundle de H5P
            // frameCss: 'path_to_h5p_frame_bundle.css', // Ruta al CSS de H5P
            displayOptions: {
      // Opciones de visualización (pueden variar según tus necesidades)
            frame: true,
        },
};

        const h5p = new H5PStandalone.H5P(h5pParams, h5pContainer)
        console.log(h5p)
        },

        movementsimulationshigh() {
            const h5pContainer = this.$refs.h5pContainer; // Asegúrate de tener un ref en tu plantilla HTML
            const h5pParams = {
    // Configuración de tu actividad H5P (puede variar según la actividad)
            content: '../../../public/h5p/preposition-of-movement-level-3-1292082403716188728.h5p', // Ruta al contenido H5P
            // frameJs: 'path_to_h5p_frame_bundle.js', // Ruta al bundle de H5P
            // frameCss: 'path_to_h5p_frame_bundle.css', // Ruta al CSS de H5P
            displayOptions: {
      // Opciones de visualización (pueden variar según tus necesidades)
            frame: true,
        },
  };

        const h5p = new H5PStandalone.H5P(h5pParams, h5pContainer)
        console.log(h5p)
        },

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