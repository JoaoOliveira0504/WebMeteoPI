<template>
  <div class="dataTable">
    <div class="table-responsive">
      <table class="table table-bordered text-center">
        <thead>
          <tr>
            <th>Distrito</th>
            <th>Previsão para as {{ time_delay1h }}</th>
            <th>Previsão para as {{ time_delay2h }}</th>
            <th>Previsão para as {{ time_delay3h }}</th>
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
    <p>A calcular previsões...</p>
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
      time_delay1h: "",
      time_delay2h: "",
      time_delay3h: "",
    };
  },
  mounted() {
    this.fetchData();
    // setInterval(this.fetchData, 300000); // 5 minutes
  },
  methods: {
    fetchData() {
      this.isLoading = true;
      this.formattedData = {};
      this.time_delay1h = "";
      this.time_delay2h = "";
      this.time_delay3h = "";
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
            rounded_datetime.getTime() - 10 * 60000 + 3600000
          );
          // Converter a hora para o formato hh:mm
          this.time_delay1h = datetime_delay.toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit",
          });
          // console.log(this.time_delay1h);
          this.time_delay2h = new Date(
            datetime_delay.getTime() + 3600000
          ).toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit",
          });
          // console.log(this.time_delay2h);
          this.time_delay3h = new Date(
            datetime_delay.getTime() + 2 * 3600000
          ).toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit",
          });
          // console.log(this.time_delay3h);
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
  background-color: #c5ecf4;
  /* Set the background color for even rows */
}

.table tbody tr:nth-child(odd) td {
  background-color: #d3d1d1;
  /* Set the background color for odd rows */
}
</style>
