<template>
    <ul>
      <li v-for="text in menuOptions" v-bind:key="text.id">
        <div class="text bold small">{{ text }}</div>
      </li>
    </ul>
</template>

<script>
export default {
  name: "HeadBanner",
  props: ['menuOptions'],
}
</script>

<style scoped>

ul {
  display: flex;
  justify-content: space-between;
  list-style: none;
  margin: 0;
  padding: 0;
}

ul li {
  display: flex;
  font-size: small;
  padding: 5px 5px;
}

</style>