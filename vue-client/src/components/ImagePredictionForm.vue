<template>
  <div class="dataTable">
    <!-- make a beautifull table with bootstrap -->
    <div class="table-responsive">

      <!-- apresentar a hora em que se está a fazer a previsão -->
      <p style="font-weight: bold">Previsão a partir das {{ date }}h</p>

      <table class="table table-bordered text-center">
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
  <div v-if="isLoading" class="text-center">
    <p>Loading...</p>
  </div>
  <p style="font-weight: bold">Intensidade Precipitação (mm/h)</p>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      formattedData: {},
      isLoading: true,
      date: "",
    };
  },
  mounted() {
    this.fetchData();
    setInterval(this.fetchData, 300000); // 5 minutes
  },

  methods: {
    fetchData() {
      this.isLoading = true;
      this.formattedData = {};
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
          this.isLoading = false;
          console.log(this.formattedData);

          // Obter a hora atual em UTC
          var current_datetime_utc = new Date();

          // Arredondar a hora atual para o múltiplo de 5 mais próximo
          var rounded_datetime = new Date(current_datetime_utc);
          rounded_datetime.setMinutes(
            Math.floor(rounded_datetime.getMinutes() / 5) * 5
          );

          // Atrasar a hora em 10 minutos
          var datetime_delay = new Date(
            rounded_datetime.getTime() - 10 * 60000
          );

          // Converter a hora para o formato hh:mm
          var datetime_local = datetime_delay.toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit",
          });

          // Atualizar a variável date
          this.date = datetime_local;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<style scoped>
/* Custom styles for the table cells */
.table td,
.table th {
  padding: 0.75rem;
  vertical-align: top;
  border-top: 1px solid #dee2e6;
}

.table th {
  vertical-align: middle;
  border-bottom: 2px solid #dee2e6;
}

/* Additional styles for better readability */

.table td:last-child,
.table th:last-child {
  padding-right: 1.5rem;
}

/* Custom colors */
.table thead th {
  background-color: #1f9cea;
  color: #000000;
  border: 1px solid #000000;
}

.table-bordered,
.table-bordered td {
  border: 1px solid #000000;
}

.table tbody tr:nth-child(even) td {
  background-color: #c5ecf4; /* Set the background color for even rows */
}

.table tbody tr:nth-child(odd) td {
  background-color: #d3d1d1; /* Set the background color for odd rows */
}
</style>
