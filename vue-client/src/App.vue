<template>
  <!-- Criar uma navbar com bootstrap -->
  <div class="container">
    <div class="row mt-3">
      <div class="col-md-12 text-center">
        <!-- <clock /> -->
        <clock ref="clock" />
      </div>
    </div>

    <div class="row">
      <div class="col-md-12">
        <div class="row">
          <div class="col-md-6">
            <image-predictions ref="imagePredictions" />
          </div>
          <div class="col-md-6">
            <Mapa ref="mapa" />
          </div>
        </div>
      </div>
    </div>
  </div>

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

<script>
import Clock from "./components/Clock.vue";
import Mapa from "./components/Mapa.vue";
import ImagePredictions from "./components/ImagePredictions.vue";

export default {
  name: "App",
  components: {
    Clock,
    Mapa,
    ImagePredictions,
  },
  mounted() {
    setInterval(() => {
      this.$refs.imagePredictions.fetchData();
      this.$refs.mapa.getRadarImage();
    }, 300000);
  },
};

</script>

<style scoped>
footer {
  background-color: #87ceeb;
  text-align: center;
  border-radius: 5px;
}
</style>
