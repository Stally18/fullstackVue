<template>
  <ul>
    <li class="nav-item dropdown">
      <a href="catalog.html"><div class="text bold">Книги</div></a>
      <ul class="dropdown-menu">
        <li><div class="dropdown-block">
          <div class="text bold">Жанры</div><br>

          <div class="text medium">Художественная литература</div>
          <div class="text medium">Книги для детей</div>
          <div class="text medium">Образование</div>
          <div class="text medium">Наука и техника</div>
          <div class="text medium">Общество</div>
          <div class="text medium">Деловая литература</div>
          <div class="text medium">Красота. Здоровье. Спорт</div>
          <div class="text medium">Увлечения</div>
          <div class="text medium">Психология</div>
          <div class="text medium">Эзотерика</div>
          <div class="text medium">Философия и религия</div>
          <div class="text medium">Искусство</div>
          <div class="text medium">Подарочные издания</div>
          <div class="text medium">Книги на иностранных языках</div>
          <div class="text medium">Книги с автографом</div>
        </div></li>
        <li><div class="dropdown-block">
          <div class="text bold">Подборки</div><br>
          <div class="text medium">Новинки литературы</div>
          <div class="text medium">Лучшие из лучших</div>
          <div class="text medium">Книги, которые помогают действовать</div>
          <div class="text medium">Скоро в продаже</div>
          <div class="text medium">Под покровом ночи</div>
        </div></li>
        <li><div class="dropdown-block">
          <div class="text bold">Издательства</div><br>
          <div class="text medium">Эксмо</div>
          <div class="text medium">АСТ</div>
          <div class="text medium">Азбука</div>
          <div class="text medium">Альпина Паблишер</div>
          <div class="text medium">Росмэн</div>
        </div></li>
        <li><div class="dropdown-block"><img src="https://img-gorod.ru/uf/49/308/49308.jpg"></div></li>
      </ul>
    </li>
    <li>
      <div class="text bold">Канцтовары</div>
    </li>
    <li>
      <div class="text bold">Сувениры</div>
    </li>
    <li>
      <div class="text bold">Игры и игрушки</div>
    </li>
    <li>
      <div class="text bold">Творчество</div>
    </li>
    <li>
      <div class="text bold">Распродажа</div>
    </li>
    <li>
      <div class="text">Акции</div>
    </li>
    <li>
      <div class="text">Подборки</div>
    </li>
    <li>
      <div class="text">Читай-журнал</div>
    </li>
    <li>
      <div class="highlight">Школа -40%</div>
    </li>
  </ul>
</template>

<script>

export default {
  name: "CategoryMenu"
}
</script>

<style scoped>

ul {
  display: flex;
  justify-content: left;
  list-style: none;
  margin: 0;
  padding: 0;
}

ul li {
  display: flex;
  font-size: small;
  padding: 5px 5px;
}

.dropdown-block {
  margin: 5px 10px 10px;
}

.dropdown-menu {
  position: relative;
  display: none;
  max-width: 1060px;
  margin-top: 26px;
  border-top: 0;
  border-radius: 0;
}

.nav-item:hover .dropdown-menu{
  position: absolute;
  display: flex;
  width: 1020px;
  justify-content: space-between;
}

</style>