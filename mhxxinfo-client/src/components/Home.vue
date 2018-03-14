<template>
    <div class="container">
        <div class="input-group col-xs-12 col-md-12 col-sm-12">
            <input type="text" placeholder="통합 검색" class="form-control" v-model="keyword" v-on:keyup.enter="allSearch(keyword)">
            <span class="input-group-btn">
                <button class="btn btn-default" type="button" @click="allSearch(keyword)"><span class="glyphicon glyphicon-search"></span></button>
            </span>
        </div><br>
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
                        console.log(response)
                    }, (error) => {
                        console.log(error)
                    })
                    break
                case 'Request':
                    axios.get('http://localhost:8000/requestQuestById/?id=' + id).then((response) => {  
                        console.log(response)
                    }, (error) => {
                        console.log(error)
                    })
                    break
                case 'Skill':
                    axios.get('http://localhost:8000/skillById/?id=' + id).then((response) => {  
                        console.log(response)
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
</style>
