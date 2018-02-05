<template>
    <div class="container">
        
        <div class="btn-group-vertical floating">
                <button class="btn btn-default" @click="scrollMove('1')">베르나 마을</button>

                <button class="btn btn-default" @click="scrollMove('2')">코코트 마을</button>

                <button class="btn btn-default" @click="scrollMove('3')">폿케 마을</button>

                <button class="btn btn-default" @click="scrollMove('4')">유쿠모 마을</button>

                <button class="btn btn-default" @click="scrollMove('5')">그 외</button>
        </div>

        <div class="panel panel-success" id="1">
            <div class="panel-heading">베르나 마을(ベルナ村)</div>
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th>의뢰명</th>
                        <th>달성조건</th>
                        <th>보상</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="row in requestQuest" v-if="row.town=='베르나 마을(ベルナ村)'">
                        <td>{{ row.requestName_kr }} {{ row.requestName }}</td>
                        <td>{{ row.condition }}</td>
                        <td>{{ row.reward }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="panel panel-success" id="2">
            <div class="panel-heading">코코트 마을(ココット村)</div>
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th>의뢰명</th>
                        <th>달성조건</th>
                        <th>보상</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="row in requestQuest" v-if="row.town=='코코트 마을(ココット村)'">
                        <td>{{ row.requestName_kr }} {{ row.requestName }}</td>
                        <td>{{ row.condition }}</td>
                        <td>{{ row.reward }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="panel panel-success" id="3">
            <div class="panel-heading">폿케 마을(ポッケ村)</div>
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th>의뢰명</th>
                        <th>달성조건</th>
                        <th>보상</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="row in requestQuest" v-if="row.town=='폿케 마을(ポッケ村)'">
                        <td>{{ row.requestName_kr }} {{ row.requestName }}</td>
                        <td>{{ row.condition }}</td>
                        <td>{{ row.reward }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="panel panel-success" id="4">
            <div class="panel-heading">유쿠모 마을(ユクモ村)</div>
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th>의뢰명</th>
                        <th>달성조건</th>
                        <th>보상</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="row in requestQuest" v-if="row.town=='유쿠모 마을(ユクモ村)'">
                        <td>{{ row.requestName_kr }} {{ row.requestName }}</td>
                        <td>{{ row.condition }}</td>
                        <td>{{ row.reward }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="panel panel-success" id="5">
            <div class="panel-heading">그 외(その他)</div>
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th>의뢰명</th>
                        <th>달성조건</th>
                        <th>보상</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="row in requestQuest" v-if="row.town=='그 외(その他)'">
                        <td>{{ row.requestName_kr }} {{ row.requestName }}</td>
                        <td>{{ row.condition }}</td>
                        <td>{{ row.reward }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'RequestQuest',
    data () {
        return {
            requestQuest: [
                {
                    'town': 'empty',
                    'requestName': 'empty',
                    'requestName_kr': 'empty',
                    'condition': 'empty',
                    'reward': 'empty',
                }
            ]
        }
    },
    methods: {
        fetchRequest: function () {
            axios.get('http://localhost:8000/requestQuest/').then((response) => {
                this.requestQuest = response.data
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
            window.scroll(0, this.getOffsetTop(document.getElementById(id)))
        }
    },
    mounted: function () {
        this.fetchRequest()
    }
}
</script>

<style>
.floating {
    position: fixed;
    top: 60%;
    right: 10px;
}
</style>