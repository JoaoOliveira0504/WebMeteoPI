<template>
  <div class="home-container">
    <!--insert image-->
    <div class="map-container">
      <div class="radar-container">
        <img :src="radarImage" alt="Mapa de Portugal" class="radar-image" />
      </div>

      <img
        src="../assets/mapaPortugal.png"
        alt="Mapa de Portugal"
        class="image"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Mapa de Portugal",
  data() {
    return {
      radarImage: null,
    };
  },
  async mounted() {
    this.getRadarImage();
    // setInterval(this.getRadarImage, 300000); // 5 minutes
  },
  methods: {
    getRadarImage() {
      console.log("Getting radar image...");
      this.radarImage = null;
      axios
        .get("http://localhost:5000/radar-image")
        .then((response) => {
          const data = response.data;
          this.radarImage = `data:image/png;base64,${data}`;
          console.log("Radar image received!");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.home-container {
  height: auto;
  width: auto;
  display: flex;
  align-items: center;
  border-color: var(--dl-color-gray-black);
  border-style: solid;
  border-width: 1px;
  background-color: #87ceeb;
  flex-direction: row;
  justify-content: center;
  vertical-align: middle;
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.map-container {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.radar-image {
  position: absolute;
  top: -32%;
  left: -37%;
  width: 180%;
  height: 184%;
}
.radar-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>
