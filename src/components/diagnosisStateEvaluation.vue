<template>
  <div class="background">
    <div class="container">
      <h1 v-if="showTitle" class="mb-4">Prepositions Quiz</h1>
      <br>
      <div v-if="!quizStarted">
        <h4>Welcome! Get ready to answer some questions about Preposition.</h4>
        <br>
        <button class="btn btn-primary" @click="startQuiz">Start</button>
      </div>
      <div v-else>
        <div v-if="visibleQuestionsIndex !== null && visibleQuestionsIndex < hiddenQuestions.length" class="quiz-question">
        <h2>Question {{ currentVisibleQuestion }}</h2>
        <p class="question" style="font-family: 'Roboto' sans-serif; font-size: 17pt;">{{ questions[hiddenQuestions[visibleQuestionsIndex] - 1].question }}</p>
        <br>
        <select v-model="selectedAnswer" :name="'student_answer' + (hiddenQuestions[visibleQuestionsIndex])" class="form-select mb-3" style="cursor: pointer;">
        <option v-for="(option, optionIndex) in questions[hiddenQuestions[visibleQuestionsIndex] - 1].options" :key="optionIndex" :value="option.value" :selected="optionIndex === 0">{{ option.text }}</option>
        </select>
  <br>
  <br>
  <v-btn class="btn-primary" color="#007bff" @click="nextQuestion" :disabled="!isAnswerSelected()">Next question <span class="mdi mdi-play"></span></v-btn>
  <router-link to="/">
    <button class="exit">Exit</button>
  </router-link>
</div>

        <div v-else-if="showMessage">
          <h4>You have finished the quiz on the topic. now send your answers</h4>
          <br>
          <button class="btn btn-primary" @click="submitAnswers">Submit</button>
        </div>
        <div v-if="showSubmitMessage">
      <div class="submit-message">
          <h1 class="mb-4">Answers Submitted! <span class="mdi mdi-check-circle"></span></h1>
          <br>
        <h5>Your answers have been submitted. Thank you for completing the quiz!</h5>
        <br>
        <h3>Let's determine your learning style, press continue</h3>
        <br>
        <router-link to="/DiagnosisStyles">
          <button class="btn btn-primary">Continue</button>
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

export default {
  data() {
    return {
      id_student: null,
      showSubmitMessage: false,
      showMessage: true,
      quizStarted: false,
      showTitle: true,
      visibleQuestionsIndex: null,
      currentVisibleQuestion: 0,
      questions: [
        {
          id: 1,
          question: 'Where is the cat? It\'s __________ the table.',
          options: [
              { text: 'on', value: 'a' },
              { text: 'in', value: 'b' },
              { text: 'under', value: 'c' },
          ]
        },
        {
          id: 2,
          question: 'We have class __________ Monday.',
          options: [
            { text: 'in', value: 'a' },
            { text: 'on', value: 'b' },
            { text: 'at', value: 'c' },
          ]
        },

        {
          id: 3,
          question: 'She walked __________ the park.',
          options: [
            { text: 'in', value: 'a' },
            { text: 'to', value: 'b' },
            { text: 'on', value: 'c' },
          ]
        },

        {          
          id: 4,
          question: 'She left her keys __________ the car.',
          options: [
            { text: 'in', value: 'a' },
            { text: 'on', value: 'b' },
            { text: 'under', value: 'c' },
          ]
        },

        {
        id: 5,
        question: "The party is going to start __________ 7 o'clock.",
  options: [
    { text: 'at', value: 'a' },
    { text: 'on', value: 'b' },
    { text: 'in', value: 'c' },
  ]
},
{
  id: 6,
  question: 'He swam __________ the river.',
  options: [
    { text: 'across', value: 'a' },
    { text: 'through', value: 'b' },
    { text: 'by', value: 'c' },
  ]
},
{
  id: 7,
  question: 'The book is __________ the shelf next to the window.',
  options: [
    { text: 'on', value: 'a' },
    { text: 'in', value: 'b' },
    { text: 'beside', value: 'c' },
  ]
},
{
  id: 8,
  question: 'He arrived __________ the morning.',
  options: [
    { text: 'at', value: 'a' },
    { text: 'in', value: 'b' },
    { text: 'on', value: 'c' },
  ]
},
{
  id: 9,
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
      answers: []
    };

  },
  mounted() {
    this.axiosCallEvaluation(); 
    },

    computed: {
    visibleQuestions() {
      return this.questions.filter(question => this.hiddenQuestions.includes(question.id));
    },
  },

  methods: {
      startQuiz() {
    this.quizStarted = true;
    this.visibleQuestionsIndex = this.hiddenQuestions.findIndex(id => id === 1);
    },

    axiosCallEvaluation(){
      const id_student = this.$store.state.userId
            axios
            .get(`/api/Activity/${id_student}`)
            .then(response => {
                this.hiddenQuestions  = response.data.data_incorrect_answer
                console.log(response.data.data_incorrect_answer)
                console.log("hidden", this.hiddenQuestions)
                this.currentVisibleQuestion = this.hiddenQuestions[0]; 

            })
            .catch(error => {
                console.log(error, 'error al capturar respuestas incorrectas')
            })},
          
            nextQuestion() {
              if (this.isAnswerSelected()) {
                this.answers.push(this.selectedAnswer);
      const nextIndex = this.visibleQuestionsIndex + 1;
      if (nextIndex < this.hiddenQuestions.length) {
        this.visibleQuestionsIndex = nextIndex;
        this.currentVisibleQuestion++
        this.selectedAnswer = null;
      } else {
        this.visibleQuestionsIndex = null;
      }
              } else {
            alert("Por favor, selecciona una respuesta antes de continuar.");
              }
    },
         submitAnswers() {
          const id_student = this.$store.state.userId
          axios.post(`/api/diagnosisEvaluation/${id_student}`, { answers : this.answers})
          .then(response => {
              console.log(response.data);
              this.showSubmitMessage = true;
              this.showMessage = false
              this.showTitle = false;
          })
          .catch(error => {
              console.log(error, 'Error al enviar')
          }) 
      },
      isAnswerSelected() {
      return this.selectedAnswer && this.selectedAnswer.length > 0;
    },


  }
};
</script>











