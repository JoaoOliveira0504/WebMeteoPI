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
      <div class="col-md-12 offset-md-3">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
          <div class="container-fluid">
            <a class="navbar-brand" href="#">WebMeteoPI</a>
          </div>
          
        </nav>
        <!-- Criar um relógio só que arredonda para baixo de 5 min e tire 5 min-->


        <!-- Criar um formulário para selecionar a imagem a ser classificada e botão para chamar a função predict com bootstrap para estilização -->

        <div class="col-md-6 offset-md-3">
          <!-- div centrada no meio -->
          <clock />

          <div class="col-md-8 offset-md-3">
            <image-prediction-form />
          </div>
        </div>

        

        <!-- Mostrar o componente RadarImage -->
        <div class="col-md-4 offset-md-3">
          <home />
        </div>

        <!-- imagem "imagens/mapa_pt.png" com uma linha à volta -->

        <div class="col-md-6 offset-md-3">

          <!-- <img src="imagens/mapa_pt.png" alt="mapa de Portugal" width="500" height="777"> -->
        </div>
      </div>

    </div>
  </div>


  <!-- Criar um footer com bootstrap 
<div class="col-md-6 offset-md-3">
          <footer class="footer mt-auto py-3 bg-light">
            <div class="container">
              <span class="text-muted">WebMeteoPI by Edgar Mendes e João Oliveira</span>
            </div>
          </footer>
        </div> -->
</template>

<style scoped>
/* Estilização do body */

body {
  background-color: #ADD8E6;
}

/* Estilização do navbar */

.navbar {
  background-color: #87CEEB;
}

/* Estilização do botão */

.btn-primary {
  background-color: #1E90FF;
  border-color: #1E90FF;
}

/* Estilização do botão quando o rato passa por cima */

.btn-primary:hover {
  background-color: #4169E1;
  border-color: #4169E1;
}

/* Estilização do botão quando está desativado */

.btn-primary:disabled {
  background-color: #B0C4DE;
  border-color: #B0C4DE;
}

/* Estilização do botão quando está desativado e o rato passa por cima */

.btn-primary:disabled:hover {
  background-color: #B0C4DE;
  border-color: #B0C4DE;
}



/* Estilização do footer */

.footer {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 60px;
  line-height: 60px;
  background-color: #f5f5f5;
}
</style>
