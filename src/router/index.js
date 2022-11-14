import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '@/views/MainView.vue'
import CatalogView from "@/views/CatalogView";

Vue.use(VueRouter)

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

const router = new VueRouter({
  routes,
})

export default router