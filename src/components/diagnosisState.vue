<template v-if="mostrarComponente">
  <div class="background">
    <div class="container">
      <div class="logos" >
        <h1 v-if="showTitle && goalCompleted !== 1" class="mb-4">Prepositions Quiz</h1>
          <v-spacer></v-spacer>
          <img src="../assets/edutlan.jpg" alt=""  style="width: 145px;"> 
        </div>
      <br>
      <div v-if="!quizStarted && goalCompleted !== 1">
        <h4>Welcome! Get ready to answer some questions about Prepositions.</h4>
        <br>
        <button class="btn btn-primary" @click="startQuiz">Start</button>
      </div>
      <div v-else>
        <div v-if="currentQuestion !== null && goalCompleted !== 1" class="quiz-question">
          <h2>Question {{ currentQuestion + 1 }}</h2>
          <p class="question" style="font-family: 'Roboto' sans-serif; font-size: 17pt;">{{ questions[currentQuestion].question }}</p>
          <br>
          <select v-model="selectedAnswer" :name="'student_answer' + (currentQuestion + 1)" class="form-select mb-3" style="cursor: pointer;">
              <option v-for="(option, optionIndex) in questions[currentQuestion].options" :key="optionIndex" :value="option.value" :selected="optionIndex === 0">{{ option.text }}</option>
          </select>
          
          <br>
          <br>
          <v-btn class="btn-primary" color="#007bff" @click="nextQuestion" :disabled="!isAnswerSelected()">Next question <span class="mdi mdi-play"></span></v-btn>
          <router-link to="/">
            <button class="exit">Exit</button>
          </router-link>
        </div>
        <div v-else-if="showMessage && goalCompleted !== 1">
          <h4>You have finished the quiz on the topic. now send your answers</h4>
          <br>
          <button class="btn btn-primary" @click="submitAnswers">Submit</button>
        </div>
        <div v-if="showSubmitMessage">
      <div class="submit-message" v-if="goalCompleted !== 1">
          <h1 class="mb-4">Answers Submitted! <span class="mdi mdi-check-circle"></span></h1>
          <br>
          <h3 class="mb-4">Need to improve with this recommended learning path</h3>
    <b-table
      :items="combinedData"
      :fields="fields"
      :tbody-tr-class="tableRowClass"
      class="mt-3"
    ></b-table>
    <br>
        <h5>Your answers have been submitted. Thank you for completing the quiz!</h5>
        <br>
        <h3>Now we start with the resources</h3>
        <br>
        <router-link to="/ActivityITS">
          <button class="btn btn-primary">View resources</button>
        </router-link> 

      </div>

      <div class="submit-message" v-if="goalCompleted == 1">
          <h1 class="mb-4">Answers Submitted! <span class="mdi mdi-check-circle"></span></h1>
          <br>
          <h3 class="mb-4">There is no learning path because no deficiencies were found in the topic.</h3>
          <br>
        <h5>But you can find resources to complement your learning, just press the continue button.</h5>
        <br>
          <a href="https://www.english-grammar.at/online_exercises/prepositions/preposition-index.htm" target="_blank"><button class="btn btn-primary">View resources</button>
</a>
<router-link to="/">
            <button class="exit">Exit</button>
          </router-link>
      </div>
    </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.background {
background-image: url('../assets/1110323_5592.jpg');
background-size: 100% 100%;
width: 100%;
min-height: 100vh;
display: flex;
justify-content: center;
align-items: center;
}


.logos {
  display: flex;

}

h1 {
color: #007bff;
font-weight: bold;
font-family: 'Roboto' sans-serif;
}

.question {
font-family: 'Roboto' sans-serif;

}

.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 60px;
  background-color: white;
  border-radius: 20px;
  margin-bottom: 150px;
}

.quiz-question {
margin-bottom: 40px;
}

.question {
font-size: 18px;
margin-bottom: 15px;
}

.form-select {
width: 100%;
padding: 10px;
font-size: 16px;
background-color: #e2e2e2;
border-radius: 20px;
}

.btn-primary {
color: #fff;
border: none;
padding: 10px 20px;
font-size: 16px;
cursor: pointer;
font-weight: bold;
font-size: 12pt;
}

button {
  margin-left: 10px;
  
}

.exit {
  width: 70px;
  text-decoration: underline;
  font-size: 13pt;

}

</style>


<script>

import axios from 'axios';
import { mapState } from 'vuex';


export default {
  data() {
    return {
      showSubmitMessage: false,
      showMessage: true,
      quizStarted: false,
      showTitle: true,
      mostrarComponente: false,
      questions: [
        {
          question: 'Where is the cat? It\'s __________ the table.',
          options: [
              { text: 'on', value: 'a' },
              { text: 'in', value: 'b' },
              { text: 'under', value: 'c' },
          ]
        },
        {
          question: 'We have class __________ Monday.',
          options: [
            { text: 'in', value: 'a' },
            { text: 'on', value: 'b' },
            { text: 'at', value: 'c' },
          ]
        },

        {
          question: 'She walked __________ the park.',
          options: [
            { text: 'in', value: 'a' },
            { text: 'to', value: 'b' },
            { text: 'on', value: 'c' },
          ]
        },

        {
          question: 'She left her keys __________ the car.',
          options: [
            { text: 'in', value: 'a' },
            { text: 'on', value: 'b' },
            { text: 'under', value: 'c' },
          ]
        },

        {
  question: "The party is going to start __________ 7 o'clock.",
  options: [
    { text: 'at', value: 'a' },
    { text: 'on', value: 'b' },
    { text: 'in', value: 'c' },
  ]
},
{
  question: 'He swam __________ the river.',
  options: [
    { text: 'across', value: 'a' },
    { text: 'through', value: 'b' },
    { text: 'by', value: 'c' },
  ]
},
{
  question: 'The book is __________ the shelf next to the window.',
  options: [
    { text: 'on', value: 'a' },
    { text: 'in', value: 'b' },
    { text: 'beside', value: 'c' },
  ]
},
{
  question: 'He arrived __________ the morning.',
  options: [
    { text: 'at', value: 'a' },
    { text: 'in', value: 'b' },
    { text: 'on', value: 'c' },
  ]
},
{
  question: 'The bird flew __________ the tree.',
  options: [
    { text: 'over', value: 'a' },
    { text: 'through', value: 'b' },
    { text: 'into', value: 'c' },
  ]
},
      ],
      currentQuestion: 0,
      selectedAnswer: null,
      answers: [], 
      recommendPath: [],
      incorrectAnswer: [],
      goalCompleted: null
    };
  },
  computed: {
...mapState(['auth']),
combinedData() {
      const combined = [...this.recommendPath];
      return combined.map(item => {
        return {
          name: item.name || item,
          goal: item.goal || '',
          lvl: item.lvl || ''
        };
      });
},


fields() {
      return [
        { key: 'name', label: 'Name' },
        { key: 'goal', label: 'Goal' },
        { key: 'lvl', label: 'Level' }
      ];
    }
  },
  mounted() {
  this.StateVerified()
},
  methods: {
    tableRowClass(item) {
      return {
        'table-success': item.goal === 'PrepositionOfPlace' && item.lvl === 'low',
        'table-info': item.goal === 'PrepositionOfPlace' && item.lvl === 'medium',
        'table-warning': item.goal === 'PrepositionOfPlace' && item.lvl === 'high',
        'table-danger': item.goal === 'PrepositionOfMovement' && item.lvl === 'low',
        'table-primary': item.goal === 'PrepositionOfMovement' && item.lvl === 'medium',
        'table-secondary': item.goal === 'PrepositionOfMovement' && item.lvl === 'high',
        'table-dark': item.goal === 'PrepositionOfTime' && item.lvl === 'low',
        'table-light': item.goal === 'PrepositionOfTime' && item.lvl === 'medium',
        'table-secondary-time': item.goal === 'PrepositionOfTime' && item.lvl === 'high'
      };
    },

    capturePath() {
      const id_student = this.$store.state.userId
      axios.get(`/api/recommendPath/${id_student}`)
      .then(response => {
        this.recommendPath = response.data.recommend_path;
        console.log(this.recommendPath)
      })
      .catch(error => {
        console.error('Error al obtener datos:', error);
      });
    },

    StateVerified(){
          const id_student = this.$store.state.userId
          axios
          .get(`/api/stateVerified/${id_student}`)
          .then(response => {
              this.goalCompleted = response.data.GoalCompleted
              if (response.data.GoalCompleted == 1) {
                this.showSubmitMessage = true;
              }
              console.log(this.goalCompleted)
          })
          .catch(error => {
              console.log(error, 'error al cargar estado')
          })},

      startQuiz() {
    this.quizStarted = true;
    this.currentQuestion = 0;
    },
    nextQuestion() {
      // Verificar si se ha seleccionado una respuesta antes de avanzar
      if (this.isAnswerSelected()) {
        this.answers.push(this.selectedAnswer);
        if (this.currentQuestion < this.questions.length - 1) {
          this.currentQuestion++;
          this.selectedAnswer = '';
        } else {
          this.currentQuestion = null;
        }
      } else {
        alert("Por favor, selecciona una respuesta antes de continuar.");
      }
    },
    previousQuestion() {
      // Retroceder a la pregunta anterior
      if (this.currentQuestion > 0) {
        this.currentQuestion--;
        this.selectedAnswer = [];
      }
    },

    isAnswerSelected() {
      return this.selectedAnswer && this.selectedAnswer.length > 0;
    },

        submitAnswers() {
          const id_student = this.$store.state.userId
          console.log('id', id_student)
          axios.post(`/api/diagnosis/${id_student}`, { answers : this.answers})
          .then(response => {
              console.log(response.data);
              this.StateVerified()
              this.showSubmitMessage = true;
              this.showMessage = false
              this.showTitle = false;
              this.capturePath()
          })
          .catch(error => {
              console.log(error, 'Error al enviar')
          }) 
      },
      checkAuthStatus() {
    console.log('Estado de autenticación:', this.auth);
  }

  }
};



</script>











