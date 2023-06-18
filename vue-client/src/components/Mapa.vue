<template>
  <div class="home-container">
    <!--insert image-->
    <img src="../assets/mapaPortugal.png" alt="Mapa de Portugal" class="image">
  </div>
</template>

<script>
export default {
  name: 'Mapa de Portugal',
};



</script>

<style scoped>
.home-container {
  height: auto;
  width: auto;
  display: flex;
  align-items: center;
  border-color: var(--dl-color-gray-black);
  border-style: solid;
  border-width: 1px;
  background-color: #87CEEB;
  flex-direction: row;
  justify-content: center;
  vertical-align: middle;
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
