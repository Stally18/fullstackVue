<template>
  <div class="collection">
    <a href="">
      <div class="collection-header bold blue">
        {{ header }}
      </div>
    </a>
    <BookCard v-for="book in books" :key="book.id" v-bind="book"></BookCard>
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
        ImageURL: 'https://img-gorod.ru/29/026/2902605_preview.jpg',
        Name: 'Стальной Алхимик. Книга 16',
        Author: 'Аракава Х.',
        Price: 999,
        type: 'book',
        Discount: 0,
        id: 1,
      },
      books: [],
      data: "",
    }
  },
  created() {
    this.get_from_api('collection', this.header);
  },
  methods: {
    async get_from_api(type, name) {
      const response = await fetch("http://localhost:8000/api/" + type + "/" + name);
      const data = await response.json();
      console.log(data);
      this.books = data;
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