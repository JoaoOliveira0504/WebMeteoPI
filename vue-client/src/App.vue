<script setup>
import { ref, watch, onMounted } from 'vue'
import axios from 'axios'

import Clock from './components/Clock.vue'
import Mapa from './components/Mapa.vue'
import RadarImage from './components/RadarImage.vue';
import ImagePredictionForm from './components/ImagePredictionForm.vue';



const API_URL = 'http://localhost:5000/predict'

const image = ref(null)

const prediction = ref(null)

const predict = async () => {
  const formData = new FormData()
  formData.append('file', image.value)
  console.log(image.value)

  try {
    const response = await axios.get(API_URL)
    console.log(response.data)
    const formattedResponse = JSON.stringify(response.data, null, 2) // Converter para JSON formatado
    prediction.value = formattedResponse
  } catch (error) {
    console.error(error)
  }
}


watch(image, () => {
  prediction.value = null
})

onMounted(() => {
  image.value = null
})

</script>

<template>
  <!-- Criar uma navbar com bootstrap -->
  <div class="container">
    

    <div class="row mt-3">
      <div class="col-md-12 text-center">
        <!-- <clock /> -->
        <clock /> <!-- Use appropriate component name here -->
      </div>
    </div>

    <div class="row">
      <div class="col-md-12">
        <div class="row">
          <div class="col-md-6">
            <image-prediction-form /> <!-- Use appropriate component name here -->
          </div>
          <div class="col-md-6">
            <Mapa /> <!-- Use appropriate component name here -->
          </div>
        </div>
      </div>
    </div>


    <div class="row">
      <div class="col-md-12 text-center">
        <!-- imagem "imagens/mapa_pt.png" com uma linha à volta -->
        <div class="col-md-6 offset-md-3">
          <!-- <img src="imagens/mapa_pt.png" alt="mapa de Portugal" width="500" height="777"> -->
        </div>
      </div>
    </div>
</div>

    <!-- Criar um footer com informação do nome do projeto e o nome dos dois desenvolvedores com bootstrap -->
    <footer class="text-center text-lg-start">
    <!-- Grid container -->
    <div class="container p-4">
      <!--Grid row-->
      <div class="row">
        <!--Grid column-->
        <div class="col-lg-6 col-md-12 mb-4 mb-md-0">
          <h5>Projeto Web Meteo com Inteligência Artificial</h5>
        </div>
        <!--Grid column-->

        <!--Grid column-->
        <div class="col-lg-6 col-md-12 mb-4 mb-md-0">
          <h5>Desenvolvido por:</h5>

          <p>
            Edgar Mendes - 2201698
            <br />
            João Oliveira - 2201705
          </p>

        </div>
        <!--Grid column-->
      </div>
      <!--Grid row-->
    </div>
    <!-- Grid container -->
  </footer>

</template>

<style scoped>

footer {
  background-color: #87CEEB;
  text-align: center;
  border-radius: 5px;
}

</style>






