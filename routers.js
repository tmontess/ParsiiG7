import { createRouter, createWebHistory } from "vue-router";
import HomePage from './components/HomePage'
import CreatePage from './components/CreatePage'
import ClientesPage from './components/ClientesPage'
import QuienesSomosPage from './components/QuienesSomosPage'
import ServiciosPage from './components/ServiciosPage'
import ExperienciaPage from './components/ExperienciaPage'


//Acá definimos las rutas
const routes = [
    {
        path: '/', //para la home page
        name: 'home',
        component:HomePage
    },
    {
        path: '/create', //para la create page
        name: 'create',
        component:CreatePage
    },
    {
        path: '/clientes', //ruta para el componente de prueba
        name: 'clientes',
        component: ClientesPage
    },

    {
        path: '/QuienesSomos', //ruta para el componente de prueba
        name: 'QuienesSomos',
        component: QuienesSomosPage
    },

    {
        path: '/ServiciosPage', //ruta para el componente de prueba
        name: 'ServiciosPage',
        component: ServiciosPage
    },

    {
        path: '/ExperienciaPage', //ruta para el componente de prueba
        name: 'ExperienciaPage',
        component: ExperienciaPage
    }

]

const router = createRouter({
    history:createWebHistory(), //Navegación por defecto
    routes,
}) 

export default router;