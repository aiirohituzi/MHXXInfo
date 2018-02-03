import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Quests from '@/components/Quests'
import Quest from '@/components/Quest'
import Kariwaza from '@/components/Kariwaza'
import RequestQuest from '@/components/RequestQuest'

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
    },
    {
      path: '/kariwaza/',
      name: 'Kariwaza',
      component: Kariwaza
    },
    {
      path: '/requestQuest/',
      name: 'RequestQuest',
      component: RequestQuest
    }
  ],
  linkActiveClass: "active"
})
