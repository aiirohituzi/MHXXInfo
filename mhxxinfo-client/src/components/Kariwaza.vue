<template>
    <div class="container">
        <div class="btn-group">
            <button class="btn btn-default">공통</button>
            <button class="btn btn-default">대검</button>
            <button class="btn btn-default">태도</button>
            <button class="btn btn-default">한손검</button>
            <button class="btn btn-default">쌍검</button>
            <button class="btn btn-default">해머</button>
            <button class="btn btn-default">수렵적</button>
            <button class="btn btn-default">랜스</button>
            <button class="btn btn-default">건랜스</button>
            <button class="btn btn-default">슬래시 액스</button>
            <button class="btn btn-default">차지 액스</button>
            <button class="btn btn-default">조충곤</button>
            <button class="btn btn-default">라이트 보우건</button>
            <button class="btn btn-default">헤비 보우건</button>
            <button class="btn btn-default">활</button>
        </div>
        <div class="btn-group-vertical floating">
            <button class="btn btn-default" @click="scrollMove(0)"><span class="glyphicon glyphicon-chevron-up" /></button>

            <button class="btn btn-default" @click="scrollMove(1)"><span class="glyphicon glyphicon-chevron-down" /></button>
        </div>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>종류</th>
                    <th>수기명</th>
                    <th>LV</th>
                    <th>개방 조건</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="row in kariwaza">
                    <td>{{ row.category }}</td>
                    <td>{{ row.kariwazaName }}</td>
                    <td>{{ row.level }}</td>
                    <td class="align-left">{{ row.condition }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Kariwaza',
    data () {
        return {
            kariwaza: [
                {
                    'category': 'empty',
                    'kariwazaName': 'empty',
                    'level': 'empty',
                    'condition': 'empty',
                }
            ],
            AllKariwaza: []
        }
    },
    methods: {
        fetchKariwaza: function () {
            axios.get('http://localhost:8000/kariwaza/').then((response) => {
                this.AllKariwaza = response.data
                this.kariwaza = response.data
                // console.log(response)
            }, (error) => {
                console.log(error)
            })
        },
        scrollMove: function(id){
            if(id==0){
                window.scroll({
                    top:0,
                    behavior: 'smooth'
                })
            } else {
                window.scroll({
                    top: document.documentElement.scrollHeight,
                    behavior: 'smooth'
                })
            }
        },
    },
    mounted: function () {
        this.fetchKariwaza()
    }
}
</script>

<style>
.floating {
    position: fixed;
    top: 80%;
    right: 10px;
}
.align-left {
    text-align: left;
}
</style>
