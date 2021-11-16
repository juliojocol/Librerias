import Vue from 'vue'
import VueRouter from 'vue-router'
import listar from '@/components/listar'
import crear from '@/components/crear'
import actualizar from '@/components/actualizar'

Vue.use(VueRouter)

const routes = [  
  {
    path: '/misitio/listar',
    name: 'Listar',
    component: listar
  },
{
    path: '/misitio/crear',
    name: 'Ingresar',
    component: crear
  },
  {
    path: '/misitio/actualizar/:id/:producto/:descripcion/:precio',
    name: 'Actualizar',
    component: actualizar
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
