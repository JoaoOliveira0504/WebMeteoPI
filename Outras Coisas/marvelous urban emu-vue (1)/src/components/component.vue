<template>
  <div class="component-container">
    <img :alt="image_alt" :src="image_src" class="component-image" />
  </div>
</template>

<script>
export default {
  name: 'AppComponent',
  props: {
    image_src: {
      type: String,
      default:
        'https://play.teleporthq.io/static/svg/placeholders/no-image.svg',
    },
    image_alt: {
      type: String,
      default: 'image',
    },
  },
}
</script>

<style scoped>
.component-container {
  display: flex;
  position: relative;
}
.component-image {
  width: 200px;
  object-fit: cover;
}
</style>
