<template>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Kariwaza',
    data () {
        return {
            skill: [
                {
                    'skillType': 'empty',
                    'skillName': 'empty',
                    'point': 'empty',
                    'effect': 'empty',
                }
            ]
        }
    },
    methods: {
        fetchSkill: function () {
            axios.get('http://localhost:8000/skill/').then((response) => {
                this.skill = response.data
                console.log(response)
            }, (error) => {
                console.log(error)
            })
        },
    },
    mounted: function () {
        this.fetchSkill()
    }
}
</script>

<style>
</style>
