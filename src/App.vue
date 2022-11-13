<template>
  <div class="wrapper">
    <header>
      <div class="headbanner1">
        <div class="container">
            <HeadBanner :menuOptions="topHeaderElements"></HeadBanner>
        </div>
      </div>
      <div class="headbanner2">
        <div class="menu">
          <div class="container">
            <HeadBanner :menuOptions="activeHeaderElements"></HeadBanner>
          </div>
        </div>
        <div class="content">
          <div class="container">
            <SearchBanner></SearchBanner>
          </div>
        </div>
      </div>
    </header>
    <main class="container">
      <div class="menu">
        <CategoryMenu></CategoryMenu>
      </div>
      <div class="banners-batch row">
        <SliderBanner></SliderBanner>
        <PromoBanner></PromoBanner>
      </div>
      <div class="banners-row row">
        <SmallPromoBanner v-bind="smallBanner1"></SmallPromoBanner>
        <SmallPromoBanner v-bind="smallBanner2"></SmallPromoBanner>
        <SmallPromoBanner v-bind="smallBanner3"></SmallPromoBanner>
      </div>
      <BookCollection header='Новинки литературы'></BookCollection>
      <BookCollection header='Новинки литературы'></BookCollection>
    </main>
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
import HeadBanner from "./components/HeadLine";
import SearchBanner from "./components/SearchBanner";
import CategoryMenu from "@/components/CategoryMenu";
import SliderBanner from "@/components/SliderBanner";
import PromoBanner from "@/components/PromoBanner";
import SmallPromoBanner from "@/components/SmallPromoBanner";
import BookCollection from "@/components/Collection/BookCollection";

// TODO: как можно сделать чтобы элемнты внутри HeadBanner отображались по разному? (вторая строка не small, войти и модуль города больше)
// TODO: совсем запутался по поводу столбцов бутстрапа, и не нашёл как сделать переезд в одну строку (как в оригинале)

export default {
  name: 'App',
  components: {
    BookCollection,
    SmallPromoBanner,
    PromoBanner,
    SliderBanner,
    CategoryMenu,
    SearchBanner,
    HeadBanner,
  },
  data() {
    return {
      topHeaderElements: [
          "Бесплатная доставка в 556 магазинов сети",
          ">85000 пунктов самовывоза по всей России",
          "8 (800) 444-8-444 – круглосуточно",
          "Обратная связь"
      ],
      activeHeaderElements: [
        "Модуль Города",
        "Адреса магазинов",
        "Доставка и оплата",
        "Бонусная программа",
        "Партнёрская программа",
        "Войти"
      ],
      smallBanner1: {
        src: 'https://img-gorod.ru/uf/49/042/49042.png',
        bold: 'Вселенная «Короля ужасов»',
        small: 'Книги и миры Стивена Кинга на одной странице'
      },
      smallBanner2: {
        src: 'https://img-gorod.ru/uf/27/914/27914.svg',
        bold: 'Книжный дозор',
        small: 'Делитесь впечатлениями, получайте бонусы'
      },
      smallBanner3: {
        src: 'https://img-gorod.ru/uf/27/915/27915.svg',
        bold: 'Игра «Книжный филворд»',
        small: 'Скидка 25% за победу'
      },
    }
  }
}
</script>

<style>
#app {
  font-family: "Segoe UI", Roboto,"Helvetica Neue","Noto Sans","Liberation Sans", "PT Sans", Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

/* leave it here */
body {
  margin: 0;
}

/* leave it here */
.wrapper {
  min-height: 100vh;
}

/* leave it here */
.container {
  margin: 0 auto;
  padding: 0 60px;
}

/* leave it here */
.headbanner1 {
  background-color: steelblue;
}

/* leave it here */
.headbanner2 {
  background-color: cornflowerblue;
  padding-bottom: 20px;
}

/* leave it here */
.menu {
  border-bottom: darkgrey solid 1px;
}

/* leave it here */
.menu a {
  text-decoration: none;
}

/* leave it here */
header .text {
  color: white;
}

/* leave it here */
main .text {
  color: black;
}

/* leave it here */
.bold {
  font-weight: bolder;
}

/* leave it here */
.large {
  font-size: large;
}

/* leave it here */
.medium {
  font-size: medium;
}

/* leave it here */
.small {
  font-size: smaller;
}

.left {
  text-align: left;
  margin-left: 15px;
}

/* leave it here */
.green {
  color: limegreen;
}

/* leave it here */
.blue {
  color: cornflowerblue;
}

/* leave it here */
.highlight {
  color: red;
}

/* leave it here */
.lowlight {
  color: gray;
}

/* leave it here */
.banners-batch {
  display: flex;
  padding-top: 100px;
}

/* leave it here */
.banners-row {
  display: flex;
  align-items: stretch;
  padding-top: 20px;
}

/* ЗДЕСЬ ТОЛЬКО ПАРАМЕТРЫ ОБЩИЕ ДЛЯ ВСЕХ БАННЕРОВ */
.banner {
  position: relative;
  display: flex;
  border: 1px solid #ddd;
  border-radius: 6px;
  padding: 5px;
  height: 100%;
  transition: all 0.1s ease-in-out;
}

.banner::after {
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
  transition: opacity 0.2s ease-in-out;
}

.banner:hover::after {
  opacity: 1;
}

.banner img {
  width: 100%;
}

</style>
