<b-table
      :items="combinedData"
      :fields="fields"
      :tbody-tr-class="tableRowClass"
      class="mt-3"
    ></b-table>


    <script>

import axios from 'axios';
import { mapState } from 'vuex';


export default {
  data() {
    return {
      recommendPath: [],
      incorrectAnswer: [],
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
  this.capturePath()()
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



  }
};



</script>
