<template>
    <div class="container">
        <ul class="list-group" v-for="quest in quests">
            <li class="list-group-item">
                <h2>
                    {{ quest.questName }}
                    {{ quest.questName_kr }}
                </h2>
                {{ quest.rating }}
                {{ quest.questMap }}
                {{ quest.condition_main }}
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
                    'questName': 'empty',
                    'questName_kr': 'empty',
                    'rating': 'empty',
                    'questMap': 'empty',
                    'condition_main': 'empty',
                }
            ]
        }
    },
    methods: {
        fetchQuests: function () {
            axios.get('http://localhost:8000/quests').then((response) => {
                this.quests = response.data
                console.log(response)
            }, (error) => {
                console.log(error)
            })
        }
    },
    mounted: function () {
        this.fetchQuests()
    }
}
</script>

<style>
</style>
