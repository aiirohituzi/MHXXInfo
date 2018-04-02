<template>
    <div class="container">
        <div class="btn-group-vertical floating">
            <button class="btn btn-default" @click="scrollMove(0)"><span class="glyphicon glyphicon-chevron-up" /></button>

            <button class="btn btn-default" @click="scrollMove(1)"><span class="glyphicon glyphicon-chevron-down" /></button>
        </div>

        <div class="input-group col-xs-12 col-md-12 col-sm-12">
            <input type="text" placeholder="스킬 검색" class="form-control" v-model="keyword" v-on:keyup="skillSearch(keyword)">
            <span class="input-group-btn">
                <button class="btn btn-default" type="button" @click="skillSearch(keyword)"><span class="glyphicon glyphicon-search"></span></button>
            </span>
        </div><br>

        <table class="table table-striped">
            <thead>
                <tr>
                    <th class="stype">계통</th>
                    <th class="sname">발동 스킬</th>
                    <th class="spoint">포인트</th>
                    <th class="seffect">스킬 효과</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="row in skill">
                    <td>{{ row.skillType }}</td>
                    <td>{{ row.skillName }}</td>
                    <td>{{ row.point }}</td>
                    <td class="align-left">{{ row.effect }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Skill',
    data () {
        return {
            skill: [
                {
                    'skillType': 'empty',
                    'skillName': 'empty',
                    'point': 'empty',
                    'effect': 'empty',
                }
            ],
            AllSkill: [],
            keyword: null,
        }
    },
    methods: {
        fetchSkill: function () {
            axios.get('http://localhost:8000/skill/').then((response) => {
                this.skill = response.data
                this.AllSkill = response.data
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
        skillSearch: function (keyword) {
            if(keyword == ''){
                this.skill = this.AllSkill
            }
            else{
                this.skill = []
                for(var i=0; i<this.AllSkill.length; i++){
                    if((this.AllSkill[i].skillType.indexOf(this.keyword) != -1) || (this.AllSkill[i].skillName.indexOf(this.keyword) != -1)){
                        this.skill.push(this.AllSkill[i])
                        // console.log(this.AllSkill[i].questName)
                        // console.log(this.AllSkill[i].questName_kr)
                    }
                }
            }
        }
    },
    mounted: function () {
        this.fetchSkill()
    }
}
</script>

<style>
.floating {
    position: fixed;
    top: 80%;
    right: 10px;
}
td {
    white-space: pre-line;
    font-size: 0.9vw;
}
th {
    font-size: 1vw;
}
.stype {
    width: 10%;
}
.sname {
    width: 20%;
}
.spoint {
    width: 6%;
}
.seffect {
    width: 65%;
}
.align-left {
    text-align: left;
}
</style>
