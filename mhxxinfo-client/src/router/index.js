import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Quests from '@/components/Quests'
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
      path: '/quests/',
      name: 'Quests',
      component: Quests
    },
    {
      path: '/quest/:id',
      name: 'Quest',
      component: Quest,
      props: true
    }
  ],
  linkActiveClass: "active"
})
