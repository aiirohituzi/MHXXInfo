<template>
    <div>
        <h2>
            {{ quests[0].questName }}
        </h2>
        {{ quests[0].contents }}
        {{ quests[0].condition }}
        {{ quests[0].reward }}
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
                console.log(quests)
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
