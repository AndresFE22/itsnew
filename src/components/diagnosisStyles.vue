<template v-for="mostrarComponente">
    <div class="background">
      <div class="container">
        <h1 class="mb-4">Test Learning Styles</h1>
        <br>
        <div v-if="!quizStarted">
          <h4>Ready! Now let's determine what your learning style is</h4>
          <br>
          <button class="btn btn-primary" @click="startQuiz">Start</button>
        </div>
        <div v-else>
          <div v-if="currentQuestion !== null" class="quiz-question">
            <h2>Question {{ currentQuestion + 1 }}</h2>
            <p class="question" style="font-family: 'Roboto' sans-serif; font-size: 17pt;">{{ questions[currentQuestion].question }}</p>
            <br>
            <select v-model="selectedAnswer" :name="'student_answer' + (currentQuestion + 1)" class="form-select mb-3" style="cursor: pointer;">
                <option v-for="(option, optionIndex) in questions[currentQuestion].options" :key="optionIndex" :value="option.value" :selected="option.text">{{ option.text }}</option>
            </select>
            <br>
            <br>
            <v-btn class="btn-primary" color="#007bff" @click="nextQuestion" :disabled="!isAnswerSelected()">Next question <span class="mdi mdi-play"></span></v-btn>
            <router-link to="/">
              <button class="exit">Exit</button>
            </router-link>
          </div>
          <div v-else-if="showText">
            <h4>Quiz completed! Click the button below to submit your answers.</h4>
            <br>
            <br>
            <button class="btn btn-primary" @click="submitAnswers">Submit Answers</button>
          </div>
          <div v-if="ShowText_l">
            <h1 class="mb-4">Answers Submitted! <span class="mdi mdi-check-circle"></span></h1>
            <br>
            <h3 class="mb-4">Great! Your learning style is the following</h3>
            <br>
            <b-table
              :items="styleList"
              :fields="fields"
              class="mt-3"
    ></b-table>
    <br>
          <h5>Your answers have been submitted. Thank you for completing the quiz!</h5>
          <br>
          <h3>Let's determine your prior knowledge, press continue</h3>
          <br>
            <router-link to="/DiagnosisState">
              <button class="btn btn-primary">Continue</button>
            </router-link>
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
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*'; 
// import { mapState } from 'vuex';

  export default {
    data() {
      return {
        quizStarted: false,
        showText: true,
        ShowText_l: false,
        mostrarComponente: false,
        questions: [
          {
            question: 'I understand better:',
            options: [
                { text: 'if I practice it.', value: 'a' },
                { text: 'if I think about it.', value: 'b' },
            
            ]
          },
          {
            question: 'I consider myself:',
            options: [
              { text: 'Realistic.', value: 'a' },
              { text: 'Innovative.', value: 'b' },
             
            ]
          },

          {
            question: 'When I think about what I did yesterday, I am more likely to do it based on:',
            options: [
              { text: 'an image.', value: 'a' },
              { text: 'words.', value: 'b' },
          
            ]
          },

          {
            question: 'I tend to:',
            options: [
              { text: 'understand the details of a subject but not clearly see its complete structure.', value: 'a' },
              { text: 'understand the complete structure but not clearly see the details.', value: 'b' },
             
            ]
          },

          {
    question: 'When I\'m learning something new, it helps me:',
    options: [
      { text: 'talk about it.', value: 'a' },
      { text: 'think about it.', value: 'b' },
    
    ]
  },
  {
    question: 'If I were a teacher, I would prefer to teach a course:',
    options: [
      { text: 'that deals with facts and real-life situations.', value: 'a' },
      { text: 'that deals with ideas and theories.', value: 'b' },
    
    ]
  },
  {
    question: 'I prefer to get new information from:',
    options: [
      { text: 'images, diagrams, charts, or maps.', value: 'a' },
      { text: 'written instructions or verbal information.', value: 'b' },
    
    ]
  },
  {
    question: 'Once I understand:',
    options: [
      { text: 'all the parts, I understand the whole.', value: 'a' },
      { text: 'the whole of something, I understand how its parts fit together.', value: 'b' },
  
    ]
  },
  {
    question: 'In a study group working with difficult material, I am more likely to:',
    options: [
      { text: 'participate and contribute ideas.', value: 'a' },
      { text: 'not participate and just listen.', value: 'b' },
     
    ]
  },
  {
    question: 'It is easier for me to:',
    options: [
      { text: 'learn facts.', value: 'a' },
      { text: 'learn concepts.', value: 'b' },
     
    ]
  },
  {
    question: 'In a book with many images and charts, I am more likely to:',
    options: [
      { text: 'carefully review the images and charts.', value: 'a' },
      { text: 'focus on the written text.', value: 'b' },
    
    ]
  },
  {
    question: 'When solving math problems:',
    options: [
      { text: 'I generally work through solutions step by step.', value: 'a' },
      { text: 'I often know what the solutions are but then have difficulty envisioning the steps to reach them.', value: 'b' },
     
    ]
  },
  {
    question: 'In the classes I have attended:',
    options: [
      { text: 'I have come to know how many of the students are.', value: 'a' },
      { text: 'I have rarely come to know how many students are.', value: 'b' },
      
    ]
  },
  {
    question: 'When reading non-fiction topics, I prefer:',
    options: [
      { text: 'something that teaches me new facts or tells me how to do something.', value: 'a' },
      { text: 'something that gives me new ideas to think about.', value: 'b' },
     
    ]
  },
  {
    question: 'I like teachers who:',
    options: [
      { text: 'use many diagrams on the board.', value: 'a' },
      { text: 'take a lot of time to explain.', value: 'b' },
 
    ]
  },

  {
    question: 'When analyzing a story or novel:',
    options: [
      { text: 'I think about the incidents and try to arrange them to shape the themes.', value: 'a' },
      { text: 'I realize what the themes are when I finish reading and then have to go back and find the incidents that demonstrate them.', value: 'b' },

    ]
  },
  {
    question: 'When I start solving a homework problem, I am more likely to:',
    options: [
      { text: 'start working on its solution immediately.', value: 'a' },
      { text: 'first try to fully understand the problem.', value: 'b' },
    
    ]
  },
  {
    question: 'I prefer the idea of:',
    options: [
      { text: 'certainty', value: 'a' },
      { text: 'theory', value: 'b' },
    ]
  },
  {
    question: 'I remember better:',
    options: [
      { text: 'what I see.', value: 'a' },
      { text: 'what I hear.', value: 'b' },
    ]
  },
  {
    question: 'It\'s more important to me that a teacher:',
    options: [
      { text: 'present the material in clear sequential steps.', value: 'a' },
      { text: 'give me an overview and relate the material to other topics.', value: 'b' },
  ]
},
        ],
        currentQuestion: 0,
        selectedAnswer: null,
        answers: [],
        styleList: []
      };
    },
    computed: {
  // ...mapState(['auth'])
    fields() {
      return [
        { key: 'dominant_style', label: 'Dominant style' },
        { key: 'style', label: 'Style' },
      ];
    }
},
  

// created() {
//     this.StateVerified();
//   },
    methods: {
      // StateVerified(){
      //       const id_student = this.$store.state.userId
      //       axios
      //       .get(`/api/styleVerified/${id_student}`)
      //       .then(response => {
      //           const resultado = response.data
      //           if (resultado.TestStyle === 1) {
      //             this.$router.push('/ActivityITS')
      //           } else {
      //             this.mostrarComponente = true
      //           }

      //       })
      //       .catch(error => {
      //           console.log(error, 'error al cargar estado')
      //       })},

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
            axios.post(`/api/test/${id_student}`, { answers : this.answers})
            .then(response => {
                console.log(response.data);
                this.showText = false;
                this.ShowText_l = true;
                this.captureStyle()
            })
            .catch(error => {
                console.log(error, 'Error al enviar')
            }) 
        },
        captureStyle() {
          const id_student = this.$store.state.userId
          axios.get(`/api/style_list/${id_student}`)
      .then(response => {
        this.styleList = response.data.style_list;
      })
      .catch(error => {
        console.error('Error al obtener datos:', error);
      });
        }

    }
  };
  </script>
  
  