<template>
    <div class="container">

        <div class="btn-group-vertical floating">
            <button class="btn btn-default" @click="scrollMove(0)"><span class="glyphicon glyphicon-chevron-up" /></button>
            <button class="btn btn-default" @click="scrollMove(1)"><span class="glyphicon glyphicon-chevron-down" /></button>
        </div>
        
        <div class="input-group col-xs-12 col-md-12 col-sm-12">
            <input type="text" placeholder="퀘스트 검색" class="form-control" v-model="keyword" v-on:keyup="questSearch(keyword)">
            <span class="input-group-btn">
                <button class="btn btn-default" type="button" @click="questSearch(keyword)"><span class="glyphicon glyphicon-search"></span></button>
            </span>
        </div><br>

        <div class="col-xs-12 col-md-12 col-sm-12">
            <div class="pull-left">
                <button v-if="(this.category != '키퀘스트')" class="btn btn-default" @click="getKeyQuest('키퀘스트')">키퀘스트</button>
                <button v-else class="btn btn-primary" @click="getKeyQuest('키퀘스트')">키퀘스트</button><br><br>
            </div>
        </div>

        <div class="col-xs-12 col-md-12 col-sm-12">
            <div class="pull-left">
                <button v-if="this.category != '마을★1'" class="btn btn-default" @click="categoryChange('마을★1')">마을★1</button>
                <button v-else class="btn btn-primary" @click="categoryChange('마을★1')">마을★1</button>

                <button v-if="this.category != '마을★2'" class="btn btn-default" @click="categoryChange('마을★2')">마을★2</button>
                <button v-else class="btn btn-primary" @click="categoryChange('마을★2')">마을★2</button>

                <button v-if="this.category != '마을★3'" class="btn btn-default" @click="categoryChange('마을★3')">마을★3</button>
                <button v-else class="btn btn-primary" @click="categoryChange('마을★3')">마을★3</button>

                <button v-if="this.category != '마을★4'" class="btn btn-default" @click="categoryChange('마을★4')">마을★4</button>
                <button v-else class="btn btn-primary" @click="categoryChange('마을★4')">마을★4</button>

                <button v-if="this.category != '마을★5'" class="btn btn-default" @click="categoryChange('마을★5')">마을★5</button>
                <button v-else class="btn btn-primary" @click="categoryChange('마을★5')">마을★5</button>        

                <button v-if="this.category != '마을★6'" class="btn btn-default" @click="categoryChange('마을★6')">마을★6</button>
                <button v-else class="btn btn-primary" @click="categoryChange('마을★6')">마을★6</button>

                <button v-if="this.category != '마을★7'" class="btn btn-default" @click="categoryChange('마을★7')">마을★7</button>
                <button v-else class="btn btn-primary" @click="categoryChange('마을★7')">마을★7</button>

                <button v-if="this.category != '마을★8'" class="btn btn-default" @click="categoryChange('마을★8')">마을★8</button>
                <button v-else class="btn btn-primary" @click="categoryChange('마을★8')">마을★8</button>

                <button v-if="this.category != '마을★9'" class="btn btn-default" @click="categoryChange('마을★9')">마을★9</button>
                <button v-else class="btn btn-primary" @click="categoryChange('마을★9')">마을★9</button>

                <button v-if="this.category != '마을★10'" class="btn btn-default" @click="categoryChange('마을★10')">마을★10</button>
                <button v-else class="btn btn-primary" @click="categoryChange('마을★10')">마을★10</button><br><br>
            </div>
        </div>

        <div class="col-xs-12 col-md-12 col-sm-12">
            <div class="pull-left">
                <button v-if="this.category != '집회소★1'" class="btn btn-default" @click="categoryChange('집회소★1')">집회소★1</button>
                <button v-else class="btn btn-primary" @click="categoryChange('집회소★1')">집회소★1</button>

                <button v-if="this.category != '집회소★2'" class="btn btn-default" @click="categoryChange('집회소★2')">집회소★2</button>
                <button v-else class="btn btn-primary" @click="categoryChange('집회소★2')">집회소★2</button>

                <button v-if="this.category != '집회소★3'" class="btn btn-default" @click="categoryChange('집회소★3')">집회소★3</button>
                <button v-else class="btn btn-primary" @click="categoryChange('집회소★3')">집회소★3</button>

                <button v-if="this.category != '집회소★4'" class="btn btn-default" @click="categoryChange('집회소★4')">집회소★4</button>
                <button v-else class="btn btn-primary" @click="categoryChange('집회소★4')">집회소★4</button>

                <button v-if="this.category != '집회소★5'" class="btn btn-default" @click="categoryChange('집회소★5')">집회소★5</button>
                <button v-else class="btn btn-primary" @click="categoryChange('집회소★5')">집회소★5</button>        

                <button v-if="this.category != '집회소★6'" class="btn btn-default" @click="categoryChange('집회소★6')">집회소★6</button>
                <button v-else class="btn btn-primary" @click="categoryChange('집회소★6')">집회소★6</button>

                <button v-if="this.category != '집회소★7'" class="btn btn-default" @click="categoryChange('집회소★7')">집회소★7</button>
                <button v-else class="btn btn-primary" @click="categoryChange('집회소★7')">집회소★7</button><br><br>
            </div>
        </div>

        <div class="col-xs-12 col-md-12 col-sm-12">
            <div class="pull-left">
                <button v-if="this.category != 'G★1'" class="btn btn-default" @click="categoryChange('G★1')">G★1</button>
                <button v-else class="btn btn-primary" @click="categoryChange('G★1')">G★1</button>

                <button v-if="this.category != 'G★2'" class="btn btn-default" @click="categoryChange('G★2')">G★2</button>
                <button v-else class="btn btn-primary" @click="categoryChange('G★2')">G★2</button>

                <button v-if="this.category != 'G★3'" class="btn btn-default" @click="categoryChange('G★3')">G★3</button>
                <button v-else class="btn btn-primary" @click="categoryChange('G★3')">G★3</button>

                <button v-if="this.category != 'G★4'" class="btn btn-default" @click="categoryChange('G★4')">G★4</button>
                <button v-else class="btn btn-primary" @click="categoryChange('G★4')">G★7</button><br><br>
            </div>
        </div>

        <div class="container">
            <div class="pull-right">
                <button class="btn btn-default" @click="changeLayout('thumbnail')">
                    <span class="glyphicon glyphicon-th-large"></span>
                </button>
                <button class="btn btn-default" @click="changeLayout('list')">
                    <span class="glyphicon glyphicon-th-list"></span>
                </button><br><br>
            </div>
        </div>


        <ul class="nav nav-tabs" v-if="this.category == '키퀘스트'">
            <li v-bind:class="{ active: isActive[0] }" @click="categoryChange_key(0, '마을★1')"><a>마을★1</a></li>
            <li v-bind:class="{ active: isActive[1] }" @click="categoryChange_key(1, '마을★2')"><a>마을★2</a></li>
            <li v-bind:class="{ active: isActive[2] }" @click="categoryChange_key(2, '마을★3')"><a>마을★3</a></li>
            <li v-bind:class="{ active: isActive[3] }" @click="categoryChange_key(3, '마을★4')"><a>마을★4</a></li>
            <li v-bind:class="{ active: isActive[4] }" @click="categoryChange_key(4, '마을★5')"><a>마을★5</a></li>
            <li v-bind:class="{ active: isActive[5] }" @click="categoryChange_key(5, '마을★6')"><a>마을★6</a></li>
            <li v-bind:class="{ active: isActive[6] }" @click="categoryChange_key(6, '마을★7')"><a>마을★7</a></li>
            <li v-bind:class="{ active: isActive[7] }" @click="categoryChange_key(7, '마을★8')"><a>마을★8</a></li>
            <li v-bind:class="{ active: isActive[8] }" @click="categoryChange_key(8, '마을★9')"><a>마을★9</a></li>
            <li v-bind:class="{ active: isActive[9] }" @click="categoryChange_key(9, '마을★10')"><a>마을★10</a></li>
        </ul>

        <ul class="nav nav-tabs" v-if="this.category == '키퀘스트'">
            <li v-bind:class="{ active: isActive[10] }" @click="categoryChange_key(10, '집회소★1')"><a>집회소★1</a></li>
            <li v-bind:class="{ active: isActive[11] }" @click="categoryChange_key(11, '집회소★2')"><a>집회소★2</a></li>
            <li v-bind:class="{ active: isActive[12] }" @click="categoryChange_key(12, '집회소★3')"><a>집회소★3</a></li>
            <li v-bind:class="{ active: isActive[13] }" @click="categoryChange_key(13, '집회소★4')"><a>집회소★4</a></li>
            <li v-bind:class="{ active: isActive[14] }" @click="categoryChange_key(14, '집회소★5')"><a>집회소★5</a></li>
            <li v-bind:class="{ active: isActive[15] }" @click="categoryChange_key(15, '집회소★6')"><a>집회소★6</a></li>
            <li v-bind:class="{ active: isActive[16] }" @click="categoryChange_key(16, '집회소★7')"><a>집회소★7</a></li>
        </ul>
        
        <ul class="nav nav-tabs" v-if="this.category == '키퀘스트'">
            <li v-bind:class="{ active: isActive[17] }" @click="categoryChange_key(17, 'G★1')"><a>G★1</a></li>
            <li v-bind:class="{ active: isActive[18] }" @click="categoryChange_key(18, 'G★2')"><a>G★2</a></li>
            <li v-bind:class="{ active: isActive[19] }" @click="categoryChange_key(19, 'G★3')"><a>G★3</a></li>
            <li v-bind:class="{ active: isActive[20] }" @click="categoryChange_key(20, 'G★4')"><a>G★4</a></li>
        </ul>


        <ul class="list-group col-xs-12 col-md-12 col-sm-12" v-if="this.layout == 'list'">
            <a class="list-group-item" @click="questDetail(quest.id)" v-for="quest in quests">
                <h3>
                    {{ quest.questName }}
                    <small>
                        {{ quest.questName_kr }}
                    </small>
                </h3>
            </a>
        </ul>
        
        <div class="row" v-if="this.layout == 'thumbnail'">
            <div class="col-sm-6 col-md-4" @click="questDetail(quest.id)" v-for="quest in quests">
                <a class="thumbnail">
                    <div class="caption">
                        <h3>{{ quest.questName }}<br>
                            <small>
                                {{ quest.questName_kr }}
                            </small>
                        </h3>
                        {{ quest.rating }}
                        {{ quest.questMap }}<br>
                        {{ quest.condition_main }}
                    </div>
                </a>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Quests',
    data () {
        return {
            category: '',
            quests: [
                {
                    'questName': 'empty',
                    'questName_kr': 'empty',
                    'rating': 'empty',
                    'questMap': 'empty',
                    'condition_main': 'empty',
                }
            ],
            keyQuests: [],
            keyword: null,
            layout: 'thumbnail',
            isActive: [true, false, ],
            AllQuest: [],
        }
    },
    methods: {
        fetchQuests: function () {
            // axios.get('http://localhost:8000/quests?rating=' + this.category).then((response) => {
            axios.get('http://localhost:8000/questsAll/').then((response) => {
                this.quests = response.data
                this.AllQuest = response.data
                // console.log(response)
            }, (error) => {
                console.log(error)
            })
        },
        categoryChange: function (category) {
            this.category = category
            // this.fetchQuests()
            this.quests = []
            
            for(var i=0; i<this.AllQuest.length; i++){
                if(this.AllQuest[i].rating == category){
                    this.quests.push(this.AllQuest[i])
                }
            }
        },
        questDetail: function (id) {
            this.$router.push({name:'Quest', params:{id:id}})
        },
        questSearch: function (keyword) {
            if(keyword == ''){
                // this.fetchQuests()
                this.quests = this.AllQuest
            }
            else{
                // axios.get('http://localhost:8000/searchQuest?keyword=' + keyword).then((response) => {
                //     this.quests = response.data
                //     console.log(response)
                // }, (error) => {
                //     console.log(error)
                // })
                this.quests = []
                for(var i=0; i<this.AllQuest.length; i++){
                    if((this.AllQuest[i].questName_kr.indexOf(this.keyword) != -1) || (this.AllQuest[i].questName.indexOf(this.keyword) != -1)){
                        this.quests.push(this.AllQuest[i])
                        // console.log(this.AllQuest[i].questName)
                        // console.log(this.AllQuest[i].questName_kr)
                    }
                }
            }
        },
        changeLayout: function (layout) {
            this.layout = layout
            console.log(this.layout)
        },
        getKeyQuest: function (category) {
            this.category = category
            axios.get('http://localhost:8000/keyQuest').then((response) => {
                this.keyQuests = response.data
                console.log(response)

                this.categoryChange_key(0, '마을★1')
            }, (error) => {
                console.log(error)
            })
        },
        categoryChange_key: function (idx, category) {
            this.isActive = [false, ]
            this.isActive[idx] = true
            this.quests = []
            
            for(var i=0; i<this.keyQuests.length; i++){
                if(this.keyQuests[i].rating == category){
                    this.quests.push(this.keyQuests[i])
                }
            }
        }
    },
    mounted: function () {
        this.fetchQuests()
    }
}
</script>

<style>
.floating {
    position: fixed;
    top: 80%;
    right: 10px;
}
</style>
