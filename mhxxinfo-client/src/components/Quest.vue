<template>
    <div class="container">
        <button type="button" class="btn btn-default pull-left" @click="Quests()">
            <span class="glyphicon glyphicon-triangle-left"></span>
        </button>
        <h2>
            {{ quests[0].questName }}
            <small>
                {{ quests[0].questName_kr }}
            </small>
        </h2>
        <table class="table table-striped">
            <tbody>
                <tr>
                    <td>등급</td>
                    <td align="left">{{ quests[0].rating }}</td>
                    <td>퀘스트 내용</td>
                    <td align="left">{{ quests[0].contents }}</td>
                </tr>
                <tr>
                    <td>맵</td>
                    <td align="left">{{ quests[0].questMap }}</td>
                    <td>제한시간</td>
                    <td align="left">{{ quests[0].questTime }}</td>
                </tr>
                <tr>
                    <td>달성조건</td>
                    <td align="left">{{ quests[0].condition_main }}</td>
                    <td>서브 달성조건</td>
                    <td align="left">{{ quests[0].condition_sub }}</td>
                </tr>
                <tr>
                    <td>계약금</td>
                    <td align="left">{{ quests[0].down_payment }}</td>
                    <td colspan="2"></td>
                </tr>
                <tr>
                    <td>메인 보수금</td>
                    <td align="left">{{ quests[0].rewardMoney_main }}</td>
                    <td>서브 보수금</td>
                    <td align="left">{{ quests[0].rewardMoney_sub }}</td>
                </tr>
                <tr>
                    <td>선행 퀘스트</td>
                    <td v-if="quests[0].precedingQuestId == '0'" colspan="3">없음</td>
                    <td v-else colspan="3" align="left"><a @click="questDetail(quests[0].precedingQuestId)">{{ precedingQuest[0].rating }} {{ precedingQuest[0].questName_kr }}</a></td>
                </tr>
                <tr>
                    <td>메인 보상</td>
                    <td align="left">{{ quests[0].reward_main }}</td>
                    <td>서브 보상</td>
                    <td align="left">{{ quests[0].reward_sub }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Quest',
    data () {
        return {
            id: this.$route.params.id,
            quests: [
                {
                    'questName': 'empty',
                    'questName_kr': 'empty',
                    'rating': 'empty',
                    'contents': 'empty',
                    'questMap': 'empty',
                    'questTime': 'empty',
                    'condition_main': 'empty',
                    'condition_sum': 'empty',
                    'down_payment': 'empty',
                    'rewardMoney_main': 'empty',
                    'rewardMoney_sub': 'empty',
                    'reward_main': 'empty',
                    'reward_sub': 'empty',
                    'precedingQuestId': 'empty',
                }
            ],
            precedingQuest: [
                {
                    'questName_kr': 'empty',
                    'rating': 'empty',
                }
            ],
        }
    },
    methods: {
        fetchQuests: function () {
            axios.get('http://localhost:8000/quest?id=' + this.id).then((response) => {
                this.quests = response.data
                console.log(response)
                axios.get('http://localhost:8000/quest?id=' + this.quests[0].precedingQuestId).then((response) => {
                    this.precedingQuest = response.data
                    console.log(response)
                }, (error) => {
                    console.log(error)
                })
            }, (error) => {
                console.log(error)
            })
        },
        Quests: function () {
            history.back()
        },
        questDetail: function (id) {
            this.$router.push({name:'Quest', params:{id:id}})
        },
    },
    mounted: function () {
        this.fetchQuests()
    }
}
</script>

<style>
</style>
