<template>
    <div class="container">
        <div class="btn-group-vertical floating" v-if="this.searchFlag">
            <button class="btn btn-default" @click="scrollMove(0)"><span class="glyphicon glyphicon-chevron-up" /></button>

            <button class="btn btn-default" @click="scrollMove(1)"><span class="glyphicon glyphicon-chevron-down" /></button>
        </div>

        <div class="input-group col-xs-12 col-md-12 col-sm-12">

            <div class="input-group-btn">
                <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-expanded="false">{{ dropdownBtn }} <span class="caret"></span></button>
                <ul class="dropdown-menu" role="menu">
                    <li @click="dropdownSelect('all', '전체검색')"><a>전체검색</a></li>
                    <li @click="dropdownSelect('Quest', '퀘스트')"><a>퀘스트</a></li>
                    <li @click="dropdownSelect('Kariwaza', '수기')"><a>수기</a></li>
                    <li @click="dropdownSelect('Request', '마을의뢰')"><a>마을의뢰</a></li>
                    <li @click="dropdownSelect('Skill', '스킬')"><a>스킬</a></li>
                </ul>
            </div>

            <div class="input-group-btn" v-if="this.searchRange != 'all'">
                <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-expanded="false">{{ dropdownBtn_sub_Select }} <span class="caret"></span></button>
                <ul class="dropdown-menu" role="menu">
                    <li v-for="item in dropdownBtn_sub" @click="dropdownSelect_sub(item)"><a>{{ item }}</a></li>
                </ul>
            </div>

            <input type="text" placeholder="통합 검색" class="form-control" v-model="keyword" v-on:keyup.enter="search(keyword)">
            <span class="input-group-btn">
                <button class="btn btn-default" type="button" @click="allSearch(keyword)"><span class="glyphicon glyphicon-search"></span></button>
            </span>
        </div><br>

        <div v-if="!this.searchFlag">
            몬스터 헌터 더블 크로스 관련 정보를 수집 및 번역합니다.<br>
            원하는 정보를 검색해주세요.
        </div>

        <div class="panel panel-info" v-if="this.detailData.active">
            <div class="panel-heading">{{ this.detailData.title }}</div>
            <div class="panel-body multiLine">{{ this.detailData.content }}</div>
        </div>

        <div class="list-group">
            <a href="#" class="list-group-item" v-for="item in result" @click="detail(item.category, item.id)">{{item.result}}</a>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Home',
    data () {
        return {
            result: [],
            dropdownBtn: '전체검색',
            dropdownBtn_sub: {},
            dropdownBtn_sub_Select: '조건검색',
            dropdownBtn_sub_list: {
                'Quest': ['조건검색', '이름', '등급', '맵', '조건'],
                'Kariwaza': ['조건검색', '종류', '이름'],
                'Request': ['조건검색', '의뢰명', '보상'],
                'Skill': ['조건검색', '계통', '발동 스킬', '효과'],
            },
            condition: null,
            keyword: null,
            searchRange: 'all',
            searchRange_sub: '',
            searchFlag: false,
            detailData: {
                'active': false,
                'title': null,
                'content': null,
            },
        }
    },
    methods: {
        search: function (keyword) {
            if(this.condition == ''){
                this.allSearch(keyword)
            } else {
                this.detailedSearch(this.condition, keyword)
            }
        },
        allSearch: function (keyword) {
            axios.get('http://localhost:8000/allSearch/?keyword=' + keyword + '&searchRange=' + this.searchRange).then((response) => {
                this.result = response.data
                // console.log(response)
                this.detailData.active = false
                if(response.data == []){
                    this.searchFlag = false
                } else {
                    this.searchFlag = true
                }
            }, (error) => {
                console.log(error)
            })
        },
        detailedSearch: function (condition, keyword) {
            axios.get('http://localhost:8000/search' + condition + '/?keyword=' + keyword + '&searchRange=' + this.searchRange_sub).then((response) => {
                this.result = response.data
                // console.log(response)
                this.detailData.active = false
                if(response.data == []){
                    this.searchFlag = false
                } else {
                    this.searchFlag = true
                }
            }, (error) => {
                console.log(error)
            })
        },
        detail: function(category, id) {
            switch(category){
                case 'Quest':
                    this.$router.push({name:'Quest', params:{id:id}})
                    break
                case 'Kariwaza':
                    axios.get('http://localhost:8000/kariwazaById/?id=' + id).then((response) => {  
                        // console.log(response.data)
                        this.detailData.title = '수기 : ' + response.data[0].kariwazaName
                        this.detailData.content = '종류 : ' + response.data[0].category + '\n' +
                                                'LV : ' + response.data[0].level + '\n' + 
                                                '개방 조건 : ' + response.data[0].condition
                        this.detailData.active = true
                    }, (error) => {
                        console.log(error)
                    })
                    break
                case 'Request':
                    axios.get('http://localhost:8000/requestQuestById/?id=' + id).then((response) => {  
                        // console.log(response)
                        this.detailData.title = '마을의뢰 : ' + response.data[0].requestName_kr + '(' + response.data[0].requestName + ')'
                        this.detailData.content = '마을 : ' + response.data[0].town + '\n\n' +
                                                '* 달성조건 *\n' + response.data[0].condition + '\n\n' +
                                                '* 보상 *\n' + response.data[0].reward
                        this.detailData.active = true
                    }, (error) => {
                        console.log(error)
                    })
                    break
                case 'Skill':
                    axios.get('http://localhost:8000/skillById/?id=' + id).then((response) => {  
                        // console.log(response)
                        this.detailData.title = '스킬 : ' + response.data[0].skillType
                        this.detailData.content = '* 발동 스킬명 *\n' + response.data[0].skillName + '\n\n' +
                                                '* 필요 포인트 *\n' + response.data[0].point + '\n\n' +
                                                '* 스킬 효과 *\n' + response.data[0].effect
                        this.detailData.active = true
                    }, (error) => {
                        console.log(error)
                    })
                    break
            }
        },
        dropdownSelect: function(range, select){
            this.searchRange=range
            this.dropdownBtn=select
            switch(range){
                case 'Quest':
                    this.dropdownBtn_sub = this.dropdownBtn_sub_list.Quest
                    this.condition = 'Quest'
                    break
                case 'Kariwaza':
                    this.dropdownBtn_sub = this.dropdownBtn_sub_list.Kariwaza
                    this.condition = 'Kariwaza'
                    break
                case 'Request':
                    this.dropdownBtn_sub = this.dropdownBtn_sub_list.Request
                    this.condition = 'Request'
                    break
                case 'Skill':
                    this.dropdownBtn_sub = this.dropdownBtn_sub_list.Skill
                    this.condition = 'Skill'
                    break
                default:
                    this.condition = ''
            }
            this.dropdownBtn_sub_Select = '조건검색'
        },
        dropdownSelect_sub: function(select){
            this.dropdownBtn_sub_Select = select
            switch(select){
                case '이름':
                    this.searchRange_sub = 'name'
                    break
                case '등급':
                    this.searchRange_sub = 'rating'
                    break
                case '맵':
                    this.searchRange_sub = 'map'
                    break
                case '조건':
                    this.searchRange_sub = 'condition'
                    break
                case '종류':
                    this.searchRange_sub = 'category'
                    break
                case '의뢰명':
                    this.searchRange_sub = 'name'
                    break
                case '보상':
                    this.searchRange_sub = 'reward'
                    break
                case '계통':
                    this.searchRange_sub = 'type'
                    break
                case '발동 스킬':
                    this.searchRange_sub = 'skillName'
                    break
                case '효과':
                    this.searchRange_sub = 'effect'
                    break
                default:
                    this.searchRange_sub = ''
            }
        }
    }
}
</script>

<style>
.multiLine {
    white-space: pre-line;
    text-align: left;
}
.dropdown-toggle{
    width: 95px;
}
.floating {
    position: fixed;
    top: 80%;
    right: 10px;
}
</style>
