<template>
  <div class="collection">
    <a href="">
      <div class="collection-header bold blue">
        {{ header }}
      </div>
    </a>
    <BookCard v-bind="book1"></BookCard>
    <BookCard v-bind="book1"></BookCard>
    <BookCard v-bind="book1"></BookCard>
    <BookCard v-bind="book1"></BookCard>
  </div>
</template>

<script>
import BookCard from "./BookCard";
export default {
  name: "BookCollection",
  components: {BookCard},
  props: {
    header: String,
  },
  data() {
    return {
      book1: {
        src: 'https://img-gorod.ru/29/026/2902605_preview.jpg',
        name: 'Стальной Алхимик. Книга 16',
        author: 'Аракава Х.',
        price: 999,
      },
    }
  }
}
</script>

<style scoped>

.collection {
  margin-left: auto;
  margin-right: auto;
  margin-top: 50px;
}

.collection a {
  text-decoration: none;
}
</style>