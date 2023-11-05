import '@fortawesome/fontawesome-free/css/all.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import '@mdi/font/css/materialdesignicons.css';
import 'vuetify/dist/vuetify.min.css';
import 'vuetify/dist/vuetify.css';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import '@fortawesome/fontawesome-free/css/all.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'

import Vue from 'vue';
import Vuetify from 'vuetify/lib';

import colors from 'vuetify/lib/util/colors'
Vue.use(Vuetify);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);


export default new Vuetify({
    icons: {
        iconfont: 'md' || 'fa' 
      },
      theme: {
        themes: {
            light: {
                background: colors.grey.lighten2, // Not automatically applied
              },
          dark: {
            background: colors.shades.white, // If not using lighten/darken, use base to return hex
          },
        },
      },
});