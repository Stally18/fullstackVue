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
    <div class="menu">
      <div class="container">
        <CategoryMenu></CategoryMenu>
      </div>
    </div>
    <div class="container">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
import HeadBanner from "./components/HeadLine";
import SearchBanner from "./components/SearchBanner";
import CategoryMenu from "./components/CategoryMenu";

// TODO: как можно сделать чтобы элемнты внутри HeadBanner отображались по разному? (вторая строка не small, войти и модуль города больше)

export default {
  name: 'App',
  components: {
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

.scored {
  text-decoration: line-through;
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

</style>
