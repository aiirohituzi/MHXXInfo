<template>
    <div class="container">
        
        <div class="input-group col-xs-12 col-md-12 col-sm-12">
            <input type="text" placeholder="퀘스트 검색" class="form-control" v-model="keyword" v-on:keyup.enter="questSearch(keyword)">
            <span class="input-group-btn">
                <button class="btn btn-default" type="button" @click="questSearch(keyword)"><span class="glyphicon glyphicon-search"></span></button>
            </span>
        </div><br>

        <div class="col-xs-12 col-md-12 col-sm-12">
            <div class="pull-left">
                <button v-if="(this.rating != '마을★1') && (this.rating != undefined)" class="btn btn-default" @click="ratingChange('마을★1')">마을★1</button>
                <button v-else class="btn btn-primary" @click="ratingChange('마을★1')">마을★1</button>

                <button v-if="this.rating != '마을★2'" class="btn btn-default" @click="ratingChange('마을★2')">마을★2</button>
                <button v-else class="btn btn-primary" @click="ratingChange('마을★2')">마을★2</button>

                <button v-if="this.rating != '마을★3'" class="btn btn-default" @click="ratingChange('마을★3')">마을★3</button>
                <button v-else class="btn btn-primary" @click="ratingChange('마을★3')">마을★3</button>

                <button v-if="this.rating != '마을★4'" class="btn btn-default" @click="ratingChange('마을★4')">마을★4</button>
                <button v-else class="btn btn-primary" @click="ratingChange('마을★4')">마을★4</button>

                <button v-if="this.rating != '마을★5'" class="btn btn-default" @click="ratingChange('마을★5')">마을★5</button>
                <button v-else class="btn btn-primary" @click="ratingChange('마을★5')">마을★5</button>        

                <button v-if="this.rating != '마을★6'" class="btn btn-default" @click="ratingChange('마을★6')">마을★6</button>
                <button v-else class="btn btn-primary" @click="ratingChange('마을★6')">마을★6</button>

                <button v-if="this.rating != '마을★7'" class="btn btn-default" @click="ratingChange('마을★7')">마을★7</button>
                <button v-else class="btn btn-primary" @click="ratingChange('마을★7')">마을★7</button>

                <button v-if="this.rating != '마을★8'" class="btn btn-default" @click="ratingChange('마을★8')">마을★8</button>
                <button v-else class="btn btn-primary" @click="ratingChange('마을★8')">마을★8</button>

                <button v-if="this.rating != '마을★9'" class="btn btn-default" @click="ratingChange('마을★9')">마을★9</button>
                <button v-else class="btn btn-primary" @click="ratingChange('마을★9')">마을★9</button>

                <button v-if="this.rating != '마을★10'" class="btn btn-default" @click="ratingChange('마을★10')">마을★10</button>
                <button v-else class="btn btn-primary" @click="ratingChange('마을★10')">마을★10</button><br><br>
            </div>
        </div>

        <div class="col-xs-12 col-md-12 col-sm-12">
            <div class="pull-left">
                <button v-if="(this.rating != '집회소★1') && (this.rating != undefined)" class="btn btn-default" @click="ratingChange('집회소★1')">집회소★1</button>
                <button v-else class="btn btn-primary" @click="ratingChange('집회소★1')">집회소★1</button>

                <button v-if="this.rating != '집회소★2'" class="btn btn-default" @click="ratingChange('집회소★2')">집회소★2</button>
                <button v-else class="btn btn-primary" @click="ratingChange('집회소★2')">집회소★2</button>

                <button v-if="this.rating != '집회소★3'" class="btn btn-default" @click="ratingChange('집회소★3')">집회소★3</button>
                <button v-else class="btn btn-primary" @click="ratingChange('집회소★3')">집회소★3</button>

                <button v-if="this.rating != '집회소★4'" class="btn btn-default" @click="ratingChange('집회소★4')">집회소★4</button>
                <button v-else class="btn btn-primary" @click="ratingChange('집회소★4')">집회소★4</button>

                <button v-if="this.rating != '집회소★5'" class="btn btn-default" @click="ratingChange('집회소★5')">집회소★5</button>
                <button v-else class="btn btn-primary" @click="ratingChange('집회소★5')">집회소★5</button>        

                <button v-if="this.rating != '집회소★6'" class="btn btn-default" @click="ratingChange('집회소★6')">집회소★6</button>
                <button v-else class="btn btn-primary" @click="ratingChange('집회소★6')">집회소★6</button>

                <button v-if="this.rating != '집회소★7'" class="btn btn-default" @click="ratingChange('집회소★7')">집회소★7</button>
                <button v-else class="btn btn-primary" @click="ratingChange('집회소★7')">집회소★7</button><br><br>
            </div>
        </div>

        <div class="col-xs-12 col-md-12 col-sm-12">
            <div class="pull-left">
                <button v-if="(this.rating != 'G★1') && (this.rating != undefined)" class="btn btn-default" @click="ratingChange('G★1')">G★1</button>
                <button v-else class="btn btn-primary" @click="ratingChange('G★1')">G★1</button>

                <button v-if="this.rating != 'G★2'" class="btn btn-default" @click="ratingChange('G★2')">G★2</button>
                <button v-else class="btn btn-primary" @click="ratingChange('G★2')">G★2</button>

                <button v-if="this.rating != 'G★3'" class="btn btn-default" @click="ratingChange('G★3')">G★3</button>
                <button v-else class="btn btn-primary" @click="ratingChange('G★3')">G★3</button>

                <button v-if="this.rating != 'G★4'" class="btn btn-default" @click="ratingChange('G★4')">G★4</button>
                <button v-else class="btn btn-primary" @click="ratingChange('G★4')">G★7</button><br><br>
            </div>
        </div>

        <ul class="list-group col-xs-12 col-md-12 col-sm-12" v-for="quest in quests">
            <li class="list-group-item" @click="questDetail(quest.id)">
                <h2>
                    {{ quest.questName }}
                    <small>
                        {{ quest.questName_kr }}
                    </small>
                </h2>
                {{ quest.rating }} / 
                {{ quest.questMap }} / 
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
            ],
            keyword: null
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
            this.$router.push({name:'Quest', params:{id:id}})
        },
        questSearch: function (keyword) {
            if(keyword == ''){
                this.fetchQuests()
            }
            else{
                axios.get('http://localhost:8000/searchQuest?keyword=' + keyword).then((response) => {
                    this.quests = response.data
                    console.log(response)
                }, (error) => {
                    console.log(error)
                })
            }
        }
    },
    mounted: function () {
        this.fetchQuests()
    }
}
</script>

<style>

</style>
