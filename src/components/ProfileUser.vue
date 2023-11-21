<!-- Use preprocessors via the lang attribute! e.g. <template lang="pug"> -->
  <template>
    <b-container fluid>
      <b-row>
        <b-col offset-md="2">
          <h1>Profile</h1>
          <hr class="my-4" />
        </b-col>
      </b-row>
      <b-row align-h="center">
        <b-col cols="6" md="2" class="my-4">
          <b-img-lazy
            thumbnail
            rounded="circle"
            :src="user.picture"
            alt="Image 1"
          >
          </b-img-lazy>
        </b-col>
  
        <b-col cols="12" md="10">
          <b-tabs content-class="mt-3" card id="app">
            <b-tab title="Info" active>
              <b-list-group>
                <b-list-group-item>
                  <span class="mdi mdi-account-box"> <b-avatar icon="Id user" /><strong>Id user</strong></span>
                  {{ user.Id }}
                </b-list-group-item>
                <b-list-group-item>
                  <span class="mdi mdi-account"> <b-avatar icon="Name" /><strong>Name</strong></span>
                  {{ user.name }}
                </b-list-group-item>
                <b-list-group-item>
                  <span class="mdi mdi-account-edit"> <b-avatar icon="Username" /><strong>Username</strong></span>
                  {{ user.users }}
                </b-list-group-item>
              </b-list-group>
              <br />
            </b-tab>
            <b-tab title="Learning path" @click="capturePath">
              <b-list-group>
                <b-list-group-item>
                  <div>
                    <b-table
      :items="combinedData"
      :fields="fields"
      :tbody-tr-class="tableRowClass"
      class="mt-3"
    ></b-table>
                  </div>
                </b-list-group-item>
              </b-list-group>
            </b-tab>
            <b-tab title="Learning style" lazy @click="captureStyle">
              <b-list-group>
                <b-list-group-item> <b-table
              :items="styleList"
              :fields="fieldStyle"
              class="mt-3"
    ></b-table></b-list-group-item>
              </b-list-group>
            </b-tab>
          </b-tabs>
        </b-col>
      </b-row>
    </b-container>
  </template>
  
  <script>
  import axios from 'axios';
  export default {

    data() {
      return {
        user: {},
        styleList: [],
        recommendPath: [],


      };
    },

    computed: {
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
    },
fieldStyle() {
      return [
        { key: 'dominant_style', label: 'Dominant style' },
        { key: 'style', label: 'Style' },
      ];
    }
  },
  
    mounted() {
      this.dataUser();
    },
  
    methods: {
      async dataUser() {
        const id_student = this.$store.state.userId;
        try {
          const response = await axios.get(`/api/dataUser/${id_student}`);
          this.user = response.data;
        } catch (error) {
          console.error(error);
        }
      },
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
      console.log('Learning Path activado');
      axios.get(`/api/recommendPath/${id_student}`)
      .then(response => {
        this.recommendPath = response.data.recommend_path;
        console.log(this.recommendPath)
        
      })
      .catch(error => {
        console.error('Error al obtener datos:', error);
      });
    },
    captureStyle() {
      console.log('Learning style activado');
          const id_student = this.$store.state.userId
          axios.get(`/api/style_list/${id_student}`)
      .then(response => {
        this.styleList = response.data.style_list;
      })
      .catch(error => {
        console.error('Error al obtener datos:', error);
      });
        }
    },
  };
  </script>
  