<template>
  <div class="card">
    <a href="">
      <div class="book-img">
        <img :src=ImageURL>
      </div>
      <div class="text">{{ Name }}</div>
      <div class="lowlight">{{ Author }}</div>
    </a><br>
    <div v-if="Discount !== 0">
         <span class="price highlight bold large">{{ disprice }}</span><span class="scored lowlight">{{ Price }} ₽</span>
    </div>
    <div v-else>
      <div class="bold large">{{ Price }} ₽</div>
    </div>
    <div class="buttons">
      <button><img src="">Купить</button>
      <div class="favourite">
        <img src="https://freepngimg.com/download/instagram/60239-like-icons-bookmark-button-computer-facebook-instagram.png">
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "BookCard",
  props: {
    ImageURL: String,
    Name: String,
    Author: String,
    Price: Number,
    Discount: Number,
  },
  data() {
    return {
      data: "",
      disprice: 0,
      disc: this.Discount,
    }
  },
  created() {
    //this.get_from_api('book', 2);
    console.log('disc calc');
    if (this.Discount > 0)
      this.disprice = (this.Price - (this.Discount/100)*this.Price).toFixed(0);
  },
  watch: {
    disc(newDisc) {
      this.disprice = (this.Price - (newDisc/100)*this.Price).toFixed(0);
    }
  },
  methods: {
    async get_from_api(type, id) {
      const response = await fetch("http://localhost:8000/api/" + type + "/" + id);
      const data = await response.json();
      console.log(data);
      this.data = data;
    }
  }
}
</script>

<style scoped>

.card {
  position: relative;
  display: inline-block;
  width: 230px;
  min-height: 400px;
  margin-top: 30px;
  margin-left: 15px;
  padding: 15px;
  transition: all 0.1s ease-in-out;
  border: 0;
}

.card a {
  text-decoration: none;
  color: black;
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
  text-align: center;
  justify-content: center;
}

.favourite img {
  height: 30px;
}

.price {
  margin-right: 30px;
}

</style>