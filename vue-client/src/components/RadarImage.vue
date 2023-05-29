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
                const response = await axios.get('http://localhost:5000/radar-image', { responseType: 'arraybuffer' });
                const base64Image = btoa(
                    new Uint8Array(response.data).reduce(
                        (data, byte) => data + String.fromCharCode(byte),
                        '',
                    ),
                );
                this.imageData = `data:image/png;base64,${base64Image}`;
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