<template>
    <!-- imagem com o tamanho flexivel do que lhe oferece -->
    <div class="radar-image">
        <img :src="imageData" alt="Radar Image" width="500" height="777" />
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    name: 'RadarImage',
    data() {
        return {
            imageData: null,
        };
    },
    mounted() {
        this.getRadarImage();
    },
    methods: {
        async getRadarImage() {
            try {
                console.log('Jorge bonito');
            } catch (error) {
                console.log(error);
            }
        },
    },
};
</script>

<style scoped>
/* Estilização da imagem */

img {
  display: block;
  margin-left: auto;
  margin-right: auto;

  border-radius: 5px;

  /* Adiciona sombra */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);

  /* Adiciona borda */
  border: 1px solid rgba(0, 0, 0, 0.5);

}

</style>