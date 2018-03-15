<template>
    <div class="container">
        <div class="input-group col-xs-12 col-md-12 col-sm-12">
            <input type="text" placeholder="통합 검색" class="form-control" v-model="keyword" v-on:keyup.enter="allSearch(keyword)">
            <span class="input-group-btn">
                <button class="btn btn-default" type="button" @click="allSearch(keyword)"><span class="glyphicon glyphicon-search"></span></button>
            </span>
        </div><br>

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
            keyword: null,
            detailData: {
                'active': false,
                'title': null,
                'content': null,
            },
        }
    },
    methods: {
        allSearch: function (keyword) {
            axios.get('http://localhost:8000/allSearch/?keyword=' + keyword).then((response) => {
                this.result = response.data
                // console.log(response)
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
                default:
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
</style>
