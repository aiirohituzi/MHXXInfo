<template>
    <div class="container">
        
        <div class="btn-group-vertical floatingMenu">
            <button class="btn btn-default" @click="scrollMove(0)"><span class="glyphicon glyphicon-chevron-up" /> TOP</button>

            <button class="btn btn-default" @click="scrollMove('1')">베르나 마을</button>

            <button class="btn btn-default" @click="scrollMove('2')">코코트 마을</button>

            <button class="btn btn-default" @click="scrollMove('3')">폿케 마을</button>

            <button class="btn btn-default" @click="scrollMove('4')">유쿠모 마을</button>

            <button class="btn btn-default" @click="scrollMove('5')">그 외</button>
        </div>

        <div class="panel panel-success" id="1">
            <div class="panel-heading">베르나 마을(ベルナ村)
                <span v-if="fold_0" class="glyphicon glyphicon-triangle-top" @click="fold_0 = !fold_0"></span>
                <span v-else class="glyphicon glyphicon-triangle-bottom" @click="fold_0 = !fold_0"></span>
            </div>
            <table class="table table-striped" v-if="fold_0">
                <thead>
                    <tr>
                        <th>의뢰명</th>
                        <th>달성조건</th>
                        <th>보상</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="row in requestQuest" v-if="row.town=='베르나 마을(ベルナ村)'">
                        <td>{{ row.requestName_kr }}<br>{{ row.requestName }}</td>
                        <td>{{ row.condition }}</td>
                        <td>{{ row.reward }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="panel panel-success" id="2">
            <div class="panel-heading">코코트 마을(ココット村)
                <span v-if="fold_1" class="glyphicon glyphicon-triangle-top" @click="fold_1 = !fold_1"></span>
                <span v-else class="glyphicon glyphicon-triangle-bottom" @click="fold_1 = !fold_1"></span>
            </div>
            <table class="table table-striped" v-if="fold_1">
                <thead>
                    <tr>
                        <th>의뢰명</th>
                        <th>달성조건</th>
                        <th>보상</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="row in requestQuest" v-if="row.town=='코코트 마을(ココット村)'">
                        <td>{{ row.requestName_kr }}<br>{{ row.requestName }}</td>
                        <td>{{ row.condition }}</td>
                        <td>{{ row.reward }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="panel panel-success" id="3">
            <div class="panel-heading">폿케 마을(ポッケ村)
                <span v-if="fold_2" class="glyphicon glyphicon-triangle-top" @click="fold_2 = !fold_2"></span>
                <span v-else class="glyphicon glyphicon-triangle-bottom" @click="fold_2 = !fold_2"></span>
            </div>
            <table class="table table-striped" v-if="fold_2">
                <thead>
                    <tr>
                        <th>의뢰명</th>
                        <th>달성조건</th>
                        <th>보상</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="row in requestQuest" v-if="row.town=='폿케 마을(ポッケ村)'">
                        <td>{{ row.requestName_kr }}<br>{{ row.requestName }}</td>
                        <td>{{ row.condition }}</td>
                        <td>{{ row.reward }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="panel panel-success" id="4">
            <div class="panel-heading">유쿠모 마을(ユクモ村)
                <span v-if="fold_3" class="glyphicon glyphicon-triangle-top" @click="fold_3 = !fold_3"></span>
                <span v-else class="glyphicon glyphicon-triangle-bottom" @click="fold_3 = !fold_3"></span>
            </div>
            <table class="table table-striped" v-if="fold_3">
                <thead>
                    <tr>
                        <th>의뢰명</th>
                        <th>달성조건</th>
                        <th>보상</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="row in requestQuest" v-if="row.town=='유쿠모 마을(ユクモ村)'">
                        <td>{{ row.requestName_kr }}<br>{{ row.requestName }}</td>
                        <td>{{ row.condition }}</td>
                        <td>{{ row.reward }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="panel panel-success" id="5">
            <div class="panel-heading">그 외(その他)
                <span v-if="fold_4" class="glyphicon glyphicon-triangle-top" @click="fold_4 = !fold_4"></span>
                <span v-else class="glyphicon glyphicon-triangle-bottom" @click="fold_4 = !fold_4"></span>
            </div>
            <table class="table table-striped" v-if="fold_4">
                <thead>
                    <tr>
                        <th>의뢰명</th>
                        <th>달성조건</th>
                        <th>보상</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="row in requestQuest" v-if="row.town=='그 외(その他)'">
                        <td>{{ row.requestName_kr }}<br>{{ row.requestName }}</td>
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
            ],
            fold_0: true,
            fold_1: true,
            fold_2: true,
            fold_3: true,
            fold_4: true,

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
            if(id==0){
                window.scroll({
                    top:0,
                    behavior: 'smooth'
                })
            } else {
                window.scroll({
                    top: this.getOffsetTop(document.getElementById(id)),
                    behavior: 'smooth'
                })
            }
        },
    },
    mounted: function () {
        this.fetchRequest()
    }
}
</script>

<style>
.floatingMenu {
    position: fixed;
    top: 60%;
    right: 10px;
}
td {
    white-space: pre-line;
    font-size: 0.9vw;
}
th {
    font-size: 1vw;
}
</style>