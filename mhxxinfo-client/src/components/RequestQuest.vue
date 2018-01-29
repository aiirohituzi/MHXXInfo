<template>
    <div class="container">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>의뢰명</th>
                    <th>달성조건</th>
                    <th>보상</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="row in requestQuest">
                    <td>{{ row.requestName }} {{ row.requestName_kr }}</td>
                    <td>{{ row.condition }}</td>
                    <td>{{ row.reward }}</td>
                </tr>
            </tbody>
        </table>
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
            axios.get('http://localhost:8000//').then((response) => {
                this.requestQuest = response.data
                // console.log(response)
            }, (error) => {
                console.log(error)
            })
        },
    },
    mounted: function () {
        this.fetchRequest()
    }
}
</script>

<style>

</style>
