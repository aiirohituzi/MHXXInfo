<template>
    <div class="container">
        <ul class="list-group" v-for="quest in quests">
            <li class="list-group-item">
                <h2>
                    {{ quest.questName }}
                </h2>
                {{ quest.rating }}
                <!-- {{ quest.contents }} -->
                {{ quest.questMap }}
                <!-- {{ quest.questTime }} -->
                {{ quest.condition_main }}
                <!-- {{ quest.condition_sub }}
                {{ quest.down_payment }}
                {{ quest.rewardMoney_main }}
                {{ quest.rewardMoney_sub }}
                {{ quest.reward_main }}
                {{ quest.reward_sub }} -->
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
                    'rating': 'empty',
                    'contents': 'empty',
                    'questMap': 'empty',
                    'questTime': 'empty',
                    'condition_main': 'empty',
                    'condition_sum': 'empty',
                    'down_payment': 'empty',
                    'rewardMoney_main': 'empty',
                    'rewardMoney_sub': 'empty',
                    'reward_main': 'empty',
                    'reward_sub': 'empty'
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
