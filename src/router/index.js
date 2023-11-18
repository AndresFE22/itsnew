import Vue from 'vue';
import VueRouter from 'vue-router';

// import verified from "../VerifiedH5p.vue";
import Home from "../components/Home.vue";
// import dia from "../components/loginU.vue";
import auth from "../components/HomeView.vue";
import profile from "../components/ProfileUser.vue";
import DiagnosisState from "../components/diagnosisState.vue";
import DiagnosisStyles from "../components/diagnosisStyles.vue";
import responseStyles from "../components/responseStyles.vue";
import ActivityGlobal from "../components/ResourcesComponent/ResourcesViewGlobal";
import ActivitySequential from "../components/ResourcesComponent/ResourcesViewSequential.vue";
import diagnosisStateEvaluation from "../components/diagnosisStateEvaluation.vue";
import ActivityITS from "../components/ActivityITS.vue";
import AcercaDe from "../components/acercaDe.vue"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/auth",
    name: "auth",
    component: auth,
  },
  {
    path: "/profile",
    name: "profile",
    component: profile,
    // meta: { requiresAuth: true }
  },
  {
    path: "/DiagnosisState",
    name: "DiagnosisState",
    component: DiagnosisState,
    // meta: { requiresAuth: true }
  },
  {
    path: "/DiagnosisStyles",
    name: "DiagnosisStyles",
    component: DiagnosisStyles,
    // meta: { requiresAuth: true }    
  },
  {
    path: "/ResponseStyles",
    name: "ResponseStyles",
    component: responseStyles,
    // meta: { requiresAuth: true }
  },
  {
    path: "/ActivityGlobal",
    name: "ActivityGlobal",
    component: ActivityGlobal,
    // meta: { requiresAuth: true }
  },
  {
    path: "/ActivitySequential",
    name: "ActivitySequential",
    component: ActivitySequential,
    // meta: { requiresAuth: true }
  },
  {
    path: "/diagnosisStateEvaluation",
    name: "diagnosisStateEvaluation",
    component: diagnosisStateEvaluation,
    // meta: { requiresAuth: true }
  },
  {
    path: "/ActivityITS",
    name: "ActivityITS",
    component: ActivityITS,
    // meta: { requiresAuth: true }
  },
  {
    path: "/AcercaDe",
    name: "AcercaDe",
    component: AcercaDe,
    // meta: { requiresAuth: true }
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
