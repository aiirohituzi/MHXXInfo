<template>
    <div>
        <h2>
            {{ questName }}
        </h2>
        {{ contents }}
        {{ condition }}
        {{ reward }}
    </div>
</template>

<script>
export default {
    name: 'Quest',
    data () {
        return {
            questName: 'aa',
            contents: 'dd',
            condition: 'ss',
            reward: 'cc'
        }
    }
}
</script>

<style>
</style>
