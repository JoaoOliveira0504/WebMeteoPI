<template>
  <div class="dataTable">
    <!-- make a beautifull table with bootstrap -->
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
/* Custom CSS for the table */
.dataTable {
  margin: 20px;
}

.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 1rem;
  background-color: #fff;
  border: 1px solid #dee2e6;
  border-radius: 4px;
}

.table thead th {
  vertical-align: middle;
  border-bottom: 2px solid #dee2e6;
  background-color: #f5f5f5;
  color: #333;
  font-weight: 600;
  text-transform: uppercase;
}

.table-striped tbody tr:nth-of-type(odd) {
  background-color: rgba(0, 0, 0, 0.05);
}

.table-bordered {
  border: 1px solid #dee2e6;
}

.table-bordered th,
.table-bordered td {
  border: 1px solid #dee2e6;
}

.table-responsive {
  display: block;
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

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
.table-striped tbody tr:hover {
  background-color: rgba(0, 0, 0, 0.075);
}

.table td:first-child,
.table th:first-child {
  padding-left: 1.5rem;
}

.table td:last-child,
.table th:last-child {
  padding-right: 1.5rem;
}

/* Custom colors */
.table thead th {
  background-color: #ccdef0;
  color: #000000;
  border: 1px solid #000000;
}

.table-striped tbody tr:nth-of-type(odd) {
  background-color: #3a81c8;
}

.table-bordered {
  border: 1px solid #000000;
}

.table-bordered th,
.table-bordered td {
  border: 1px solid #000000;
}

.table-bordered tbody td:first-child {
  border-left: none;
}

.table-bordered tbody td:last-child {
  border-right: none;
}

.table-bordered tbody tr:first-child td {
  border-top: none;
}

.table-bordered tbody tr:last-child td {
  border-bottom: none;
}


</style>
