<template>
  <div class="clock-container col-md-12 offset-md-3"> <!-- mudar para col-md-8 offset-md-3 quando conseguir centrar a div -->
    <div class="clock-time">{{ formattedTime }}</div>
    <div class="clock-date">{{ formattedDate }}</div>
    <div>
      <div class="greeting">
        <img :src="iconPath" :alt="iconAlt" class="daytime-icon" :style="{ filter: iconFilter }">
        <span>{{ greeting }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formattedTime: '',
      formattedDate: '',
      greeting: '',
      iconPath: '',
      iconAlt: ''
    };
  },
  mounted() {
    this.updateTime();
    setInterval(this.updateTime, 300000); // Atualiza a cada 5 minutos (5 * 60 * 1000 ms)
  },
  methods: {
    updateTime() {
      const now = new Date();

      // Arredonda os minutos para o múltiplo mais próximo de 5
      const roundedMinutes = Math.round(now.getMinutes() / 5) * 5;

      // Subtrai 5 minutos
      now.setMinutes(roundedMinutes - 5);

      const timeOptions = {
        hour: 'numeric',
        minute: 'numeric'
      };
      this.formattedTime = now.toLocaleString('pt-PT', timeOptions);

      const dateOptions = {
        weekday: 'long',
        day: 'numeric',
        month: 'long',
        year: 'numeric'
      };
      this.formattedDate = now.toLocaleString('pt-PT', dateOptions);

      const hour = now.getHours();
      if (hour >= 5 && hour < 12) {
        this.greeting = 'Bom dia!';
        this.iconPath = '/sun.png'; // Caminho relativo à pasta "public"
        this.iconAlt = 'Ícone do Sol';
      } else if (hour >= 12 && hour < 18) {
        this.greeting = 'Boa tarde!';
        this.iconPath = '/sun.png'; // Caminho relativo à pasta "public"
        this.iconAlt = 'Ícone do Sol';
      } else {
        this.greeting = 'Boa noite!';
        this.iconPath = '/moon.png'; // Caminho relativo à pasta "public"
        this.iconAlt = 'Ícone da Lua';
      }
    }
  }
};
</script>

<style scoped>
.clock-container {
  text-align: right;
  margin-bottom: 20px;
  background-color: #87CEEB;
  padding: 10px;
  border-radius: 5px;

  /* Adiciona sombra */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);

  /* Adiciona borda */
  border: 1px solid rgba(0, 0, 0, 0.5);
}

.clock-time {
  font-size: 30px;
  font-weight: bold;
}

.clock-date {
  font-size: 18px;
  margin-bottom: 10px;
}

.greeting {
  display: flex;
  justify-content: end;
  font-size: 24px;
  font-weight: bold;
}

.icon-container {
  text-align: center;
  margin-top: 10px;
}

/* .greeting {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  font-weight: bold;
} */

.daytime-icon {
  height: 24px;
  width: 24px;
  margin-right: 25px;
}
</style>
