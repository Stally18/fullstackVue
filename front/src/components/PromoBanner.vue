<template>
  <div class="col-3">
    <div class="banner">
      <button class="btn"><div class="bold">Лучшие из лучших</div></button>
      <div class="center-logo">
        <img src="https://www.chitai-gorod.ru/ii/img/bestsell/bestsell.svg">
      </div>
      <div class="textblock">
        <div class="green bold small">Подборка лучших* книг</div>
        <div class="text small">*На основании продаж интернет-магазина</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PromoBanner"
}
</script>

<style scoped>
/* здесь возможно поможет flex-direction, тогда можно всем баннерам флекс задать */
.banner {
  flex-direction: column;
  justify-content: space-between;
  text-align: center;
}

.center-logo img {
  width: 40%;
}

.textblock {
  padding-bottom: 20px;
  margin: 0 20px;
}

button {
  width: 100%;
  height: 60px;
  background-color: limegreen;
  color: #fff;
  border-radius: 0;
}
</style>