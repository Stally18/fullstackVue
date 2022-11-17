<template>
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
</template>

<script>
import BookCollection from "@/components/Collection/BookCollection";
import SmallPromoBanner from "@/components/SmallPromoBanner";
import PromoBanner from "@/components/PromoBanner";
import SliderBanner from "@/components/SliderBanner";

export default {
  name: "MainView",
  components: {
    BookCollection,
    SmallPromoBanner,
    PromoBanner,
    SliderBanner,
  },
  data() {
    return {
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

.banners-batch {
  display: flex;
  padding-top: 100px;
}

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