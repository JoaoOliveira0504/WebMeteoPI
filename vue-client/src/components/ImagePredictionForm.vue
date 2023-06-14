<template>
  <div class="hello">
    <!-- make a beautifull table with bootstrap -->
    <h1>Previsão de precipitação</h1>
    <div class="table-responsive">
    <table class="table table-striped table-bordered">
      <thead>
        <tr>
          <th>Distrito</th>
          <th>1 hora de diferença</th>
          <th>2 horas de diferença</th>
          <th>3 horas de diferença</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, key) in formattedData" :key="key">
          <td>{{ key }}</td>
          <td>{{ item[0] }}</td>
          <td>{{ item[1] }}</td>
          <td>{{ item[2] }}</td>
        </tr>
      </tbody>
    </table>
  </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import axios from "axios";

export default {
  data() {
    return {
      formattedData: {},
    };
  },
  methods: {
  fetchData() {
    console.log("Fetching data...");

    axios
      .get("http://localhost:5000/process_image")
      .then((response) => {
        const data = response.data;

        for (const [key, value] of Object.entries(data)) {
          for (const [key2, value2] of Object.entries(value)) {
            if (!this.formattedData[key2]) {
              this.formattedData[key2] = [];
            }
            this.formattedData[key2].push(value2);
          }
        }
        // console.log(this.formattedData);

        setTimeout(() => {
          this.fetchData();
        }, 300000); // Fetch data again after 5 minutes
      })
      .catch((error) => {
        console.error(error);

        setTimeout(() => {
          this.fetchData();
        }, 300000); // Fetch data again after 5 minutes in case of error
      });
  }
},

  mounted() {
    this.fetchData();    
  },

};
</script>

<style scoped>
/* CSS styles */
/* Make sure that the <td> text are centered */
td, th {
  text-align: center;
}
</style>
