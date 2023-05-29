<template>
    <div>
        <h2>Image Prediction</h2>
        <form @submit.prevent="predict">
            <div class="form-group">
                <label for="districts">Select district:</label>
                <select class="form-control" id="districts" v-model="selectedDistrict">
                    <option v-for="(districtName, districtCode) in districts" :value="districtCode">{{ districtName }}
                    </option>
                </select>
            </div>
            <button class="btn btn-primary" :disabled="!selectedDistrict">Predict</button>
        </form>
        <div v-if="prediction" class="mt-4">
            <h3>Prediction</h3>
            <pre>{{ prediction }}</pre>
        </div>
    </div>
</template>
  
<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const API_URL = 'http://localhost:5000/process_image'
const DISTRICTS_API_URL = 'http://localhost:5000/estacoes'

export default {
    data() {
        return {
            selectedDistrict: null,
            prediction: null,
            districts: {}
        }
    },
    methods: {
        async predict() {
            try {
                const response = await axios.post(API_URL, { 'selected-district': this.selectedDistrict })
                console.log(this.selectedDistrict)
                console.log(response.data)
                this.prediction = JSON.stringify(response.data, null, 2)
            } catch (error) {
                console.error(error)
            }
        }
    },
    async mounted() {
        try {
            const response = await axios.get(DISTRICTS_API_URL)
            this.districts = response.data
        } catch (error) {
            console.error(error)
        }
    }
}
</script>
  
<style scoped>
/* CSS styles */
</style>
  