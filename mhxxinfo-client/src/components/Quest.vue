<template>
    <div class="container">
        <ul class="list-group" v-for="quest in quests">
            <li class="list-group-item">
                <h2>
                    {{ quest.questName }}
                </h2>
                {{ quest.contents }}
                {{ quest.condition }}
                {{ quest.reward }}
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Quest',
    data () {
        return {
            quests: [
                {
                    'questName': '',
                    'contents': '',
                    'condition': '',
                    'reward': '',
                }
            ]
        }
    },
    methods: {
        fetchQeusts: function () {
            axios.get('http://localhost:8000/quest').then((response) => {
                this.quests = response.data
                // console.log(response)
            }, (error) => {
                console.log(error)
            })
        }
    },
    mounted: function () {
        this.fetchQeusts()
    }
}
</script>

<style>
</style>
