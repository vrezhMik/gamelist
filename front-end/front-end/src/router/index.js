import Vue from "vue";
import VueRouter from "vue-router";
import SharkComp from "@/components/Shark.vue";
import GamesComp from "@/components/Games.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/shark",
    name: "Shark",
    component: SharkComp,
  },
  {
    path: "/games",
    name: "Games",
    component: GamesComp,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
