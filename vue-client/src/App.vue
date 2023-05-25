<script setup>
import { ref, watch, onMounted } from 'vue'
import axios from 'axios'

import Clock from './components/Clock.vue'
import home from './components/home.vue'


const API_URL = 'http://localhost:5000/predict'

const image = ref(null)

const prediction = ref(null)

const predict = async () => {
  const formData = new FormData()
  formData.append('file', image.value)
  console.log(image.value)

  try {
    const response = await axios.post(API_URL, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })

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
          
          <h2>Image Prediction</h2>
          <div class="form-group">
            <label for="image">Select an image:</label>
            <input type="file" class="form-control-file" id="image" @change="image = $event.target.files[0]" />
          </div>
          <button class="btn btn-primary" @click="predict" :disabled="!image">Predict</button>
          <div v-if="prediction" class="mt-4">
            <h3>Prediction</h3>
            <pre v-html="prediction"></pre>
          </div>
        </div>

        <!-- imagem "imagens/mapa_pt.png" com uma linha à volta -->

        <div class="col-md-6 offset-md-3">
          
         <!-- <img src="imagens/mapa_pt.png" alt="mapa de Portugal" width="500" height="777"> -->
        </div>
      </div>
    </div>
  </div>
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
