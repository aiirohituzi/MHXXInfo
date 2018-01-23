<template>
    <div class="container">
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
                    <td>{{ row.condition }}</td>
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
            ]
        }
    },
    methods: {
        fetchQuests: function () {
            axios.get('http://localhost:8000/kariwaza/').then((response) => {
                this.kariwaza = response.data
                // console.log(response)
            }, (error) => {
                console.log(error)
            })
        },
    },
    mounted: function () {
        this.fetchQuests()
    }
}
</script>

<style>

</style>
