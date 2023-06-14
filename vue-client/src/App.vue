<script setup>
import { ref, watch, onMounted } from 'vue'
import axios from 'axios'

import Clock from './components/Clock.vue'
import home from './components/home.vue'
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
    <div class="row">
      <div class="col-md-12">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
          <div class="container-fluid">
            <a class="navbar-brand" href="#">WebMeteoPI</a>
          </div>
        </nav>
      </div>
    </div>

    <div class="row">
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
            <home /> <!-- Use appropriate component name here -->
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
</template>






