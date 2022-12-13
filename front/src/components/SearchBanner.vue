<template>
  <div id="content">
    <div class="logo">
      <router-link class="nav-link" :to="{name: 'Main'}">
        <img src="https://www.chitai-gorod.ru/ii/img/logo/main_logo_white.svg">
      </router-link>
    </div>
    <label>
      <input placeholder="Поиск..."/>
      <button>
        <img src="https://d1bd5u3q1t3nu7.cloudfront.net/icons/297/magnifying-glass-icon-256.png" height="40px">
      </button>
    </label>
    <div class="basket">
      <div class="logo">
        <img src="https://www.chitai-gorod.ru/ii/img/general/basket.svg">
      </div>
      <div class="text">
        <div class="text-item"><div class="bold small">Корзина:</div> <div class="bold">а:</div></div>
        <div class="text-item"><div class="small">Закладки:</div> <div class="small">0</div></div>
        <div class="text-item"><div class="small">Резерв:</div> <div class="small">0</div></div>
      </div>
    </div>
  </div>
</template>

<script>

// TODO: пощему ноль съезжаит

export default {
  name: "SearchBanner"
}
</script>

<style scoped>

#content {
  justify-content: space-between;
  padding-top: 24px;
  display: flex;
}

.basket {
  display: flex;
  margin-right: 20px;
}

.basket .text {
  width: 80px;
}

.basket .text .bold {
  padding-bottom: 5px;
}

.basket .text .text-item {
  display: flex;
  justify-content: space-between;
}

.basket .logo {
  margin-right: 20px;
}

/* только так сработало на Vue, может это плохо? без флекса кнопка уезжала вверх, а поле ввода вниз */
label {
  display: flex;
}

input {
  border: 0;
  height: 40px;
  border-radius: 5px 0 0 5px;
  width: 400px;
  padding: 0 10px;
}

button {
  height: 40px;
  border: 0;
  background-color: darkslateblue;
  border-radius: 0 5px 5px 0;
}
</style>