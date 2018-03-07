<template>
    <div class="container">
        <div class="btn-group floating-bottom">
            <button class="btn btn-default" @click="scrollMove(1)">공통</button>
            <button class="btn btn-default" @click="scrollMove(11)">대검</button>
            <button class="btn btn-default" @click="scrollMove(23)">태도</button>
            <button class="btn btn-default" @click="scrollMove(35)">한손검</button>
            <button class="btn btn-default" @click="scrollMove(47)">쌍검</button>
            <button class="btn btn-default" @click="scrollMove(59)">해머</button>
            <button class="btn btn-default" @click="scrollMove(71)">수렵적</button>
            <button class="btn btn-default" @click="scrollMove(83)">랜스</button>
            <button class="btn btn-default" @click="scrollMove(95)">건랜스</button>
            <button class="btn btn-default" @click="scrollMove(107)">슬래시 액스</button>
            <button class="btn btn-default" @click="scrollMove(119)">차지 액스</button>
            <button class="btn btn-default" @click="scrollMove(131)">조충곤</button>
            <button class="btn btn-default" @click="scrollMove(143)">라이트 보우건</button>
            <button class="btn btn-default" @click="scrollMove(155)">헤비 보우건</button>
            <button class="btn btn-default" @click="scrollMove(167)">활</button>
        </div>
        <div class="btn-group-vertical floating">
            <button class="btn btn-default" @click="scrollMove(-1)"><span class="glyphicon glyphicon-chevron-up" /></button>
            <button class="btn btn-default" @click="scrollMove(0)"><span class="glyphicon glyphicon-chevron-down" /></button>
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
                <tr v-for="row in kariwaza" :id="row.id">
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
                console.log(response)
            }, (error) => {
                console.log(error)
            })
        },
        getOffsetTop: function(el) {
            var top = 0;
            if(el.offsetParent){
                do{
                    top += el.offsetTop
                } while(el = el.offsetParent)
                return [top-55]
            }
        },
        scrollMove: function(id){
            switch(id){
                case -1:
                    window.scroll({
                        top:0,
                        behavior: 'smooth'
                    })
                    break
                case 0:
                    window.scroll({
                        top: document.documentElement.scrollHeight,
                        behavior: 'smooth'
                    })
                    break
                default:
                    window.scroll({
                        top: this.getOffsetTop(document.getElementById(id)),
                        behavior: 'smooth'
                    })
            }
        }
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
.floating-bottom {
    position: fixed;
    right: 10px;
    bottom: 10px;
}
.align-left {
    text-align: left;
}
</style>
