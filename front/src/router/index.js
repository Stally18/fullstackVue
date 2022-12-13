import * as VueRouter from 'vue-router'
import MainView from '../views/MainView.vue'
import CatalogView from "../views/CatalogView";

const routes = [
  {
    path: '/',
    name: 'Main',
    component: MainView
  },
  {
    path: '/catalog',
    name: 'Catalog',
    component: CatalogView
  },
]

const router = VueRouter.createRouter({
  history: VueRouter.createWebHashHistory(),
  routes,
})

export default router