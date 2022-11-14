<template>
  <div class="catalog">
    <div class="row">
      <div class="col-md-3">
        <div class="text bold">Читай город рекомендует</div>
        <div class="text">Новинки литературы</div>
        <div class="text">Лучшие из лучших</div>
        <div class="text">Книги, которые помогают действовать</div>
        <div class="text">Скоро в продаже</div>
        <div class="text">Под покровом ночи</div><br>
        <div class="text bold">Категории</div>
        <div class="text">Художественная литература</div>
        <div class="text">Книги для детей</div>
        <div class="text">Образование</div>
        <div class="text">Наука и техника</div>
        <div class="text">Общество</div>
        <div class="text">Деловая литература</div>
        <div class="text">Красота. Здоровье. Спорт</div>
        <div class="text">Увлечения</div>
        <div class="text">Психология</div>
        <div class="text">Эзотерика</div>
        <div class="text">Философия и религия</div>
        <div class="text">Искусство</div>
        <div class="text">Подарочные издания</div>
        <div class="text">Книги на иностранных языках</div>
        <div class="text">Книги с автографом</div>
      </div>
      <div class="col-md-9">
        Книжный магазин > Книги
        <BookCollection></BookCollection>
        <BookCollection></BookCollection>
      </div>
    </div>
  </div>
</template>

<script>
import BookCollection from "@/components/Collection/BookCollection";
export default {
  name: "CatalogView",
  components: {BookCollection}
}
</script>

<style scoped>

</style>