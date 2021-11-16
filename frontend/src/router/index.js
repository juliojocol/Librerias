import Vue from 'vue'
import VueRouter from 'vue-router'
import Listar from '@/components/Listar'
import Crear from '@/components/Crear'
import Actualizar from '@/components/Actualizar'

Vue.use(VueRouter)

const routes = [  
  {
    path: '/misitio/listar',
    name: 'Listar',
    component: Listar
  },
{
    path: '/misitio/crear',
    name: 'Crear',
    component: Crear
  },
  {
    path: '/misitio/actualizar/',
    name: 'Actualizar',
    component: Actualizar
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
