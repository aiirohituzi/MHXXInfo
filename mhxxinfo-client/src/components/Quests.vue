<template>
    <div class="container">
        <div class="pull-left">
            <button v-if="(this.rating != '마을★1') && (this.rating != undefined)" class="btn btn-default" @click="ratingChange('마을★1')">마을★1</button>
            <button v-else class="btn btn-primary" @click="ratingChange('마을★1')">마을★1</button>

            <button v-if="this.rating != '마을★2'" class="btn btn-default" @click="ratingChange('마을★2')">마을★2</button>
            <button v-else class="btn btn-primary" @click="ratingChange('마을★2')">마을★2</button>

            <button v-if="this.rating != '마을★3'" class="btn btn-default" @click="ratingChange('마을★3')">마을★3</button>
            <button v-else class="btn btn-primary" @click="ratingChange('마을★3')">마을★3</button>
        </div><br><br>
        <ul class="list-group" v-for="quest in quests">
            <li class="list-group-item" @click="questDetail(quest.id)">
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
    name: 'Quests',
    data () {
        return {
            rating: '마을★1',
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
            axios.get('http://localhost:8000/quests?rating=' + this.rating).then((response) => {
                this.quests = response.data
                console.log(response)
            }, (error) => {
                console.log(error)
            })
        },
        ratingChange: function (rating) {
            this.rating = rating
            this.fetchQuests()
        },
        questDetail: function (id) {
            console.log('aaaa')
            this.$router.push({name:'Quest', params:{id:id}})
        },
    },
    mounted: function () {
        this.fetchQuests()
    }
}
</script>

<style>
</style>
