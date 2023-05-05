import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import IntroView from "../views/IntroView.vue";
import Game from "../views/Game.vue";
import Rank from "../views/Rank.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/intro",
    name: "intro",
    component: IntroView,
  },
  {
    path: "/rank",
    name: "Rank",
    component: Rank,
  },
  {
    path: "/game",
    name: "game",
    component: Game,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
