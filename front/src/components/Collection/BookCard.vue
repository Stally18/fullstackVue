<template>
  <div class="card">
    <a href="">
      <div class="book-img">
        <img :src=src>
      </div>
      <div class="text">{{ name }}</div>
      <div class="lowlight">{{ author }}</div>
    </a><br>
    <div class="bold large">{{ price }} ₽</div>
    <div class="buttons">
      <button><img src="">Купить</button>
      <div class="favourite">
        <img src="https://freepngimg.com/download/instagram/60239-like-icons-bookmark-button-computer-facebook-instagram.png" height="40px">
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "BookCard",
  props: {
    src: String,
    name: String,
    author: String,
    price: Number,
  }
}
</script>

<style scoped>

.card {
  position: relative;
  display: inline-block;
  width: 230px;
  margin-top: 30px;
  margin-left: 15px;
  padding: 15px;
  transition: all 0.1s ease-in-out;
  border: 0;
}

.card a {
  text-decoration: none;
}

.card a img {
  height: 200px;
}

.card .book-img {
  text-align: center;
  padding-bottom: 20px;
}

.card::after {
  content: '';
  position: absolute;
  z-index: -1;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  border-radius: 5px;
  box-shadow: 0 5px 10px rgba(0,0,0,0.3);
  transition: opacity 0.1s ease-in-out;
}

.card:hover::after {
  opacity: 1;
}

.buttons {
  margin-top: 15px;
  height: 40px;
  display: flex;
  justify-content: space-between;
}

/* тут объединить - свойства обоих кнопок в button, остальное отдельно */
button {
  width: 70%;
  background-color: cornflowerblue;
  color: #fff;
  border-radius: 5px;
  border: 0;
}

.favourite {
  width: 20%;
  background-color: whitesmoke;
  border-radius: 5px;
  border: 0;
}

.favourite img {
  height: 40px;
}

</style>