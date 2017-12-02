import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Quest from '@/components/Quest'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/quest/',
      name: 'Quest',
      component: Quest
    }
  ]
})
