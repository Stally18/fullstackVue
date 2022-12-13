<template>
    <div class="col-lg-4 col-xl-12">
      <div class="banner">
        <div class="left-logo">
          <img :src="src">
        </div>
        <div>
          <div class="blue bold small left">{{bold}}</div>
          <div class="text small left">{{ small }}</div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: "SmallPromoBanner",
  props: {
    src: String,
    bold: String,
    small: String,
  }
}
</script>

<style scoped>

.left-logo {
  height: 90px;
}

.left-logo img {
  background-color: lightgray;
  min-height: 90px;
  width: auto;
  height: 100%;
}

.col-xl-12 {
  padding-bottom: 5px;
}

</style>