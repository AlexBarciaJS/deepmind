<template>
  <div class="content">
    <div class="chat-container">
      <!-- Sección de Respuesta -->
      <div class="respuesta-box">
        <span>respuesta</span>
      </div>

      <!-- Sección del Chat -->
      <div class="chat-box">
        <chat-form></chat-form>
      </div>
    </div>
  </div>
</template>

<script>
import { ChatForm } from "@/pages";

export default {
  components: {
    ChatForm,
  },
};
</script>

<style scoped>
/* Contenedor principal con Flexbox */
.chat-container {
  display: flex;
  flex-direction: column;
  align-items: center;  /* Centra horizontalmente */
  justify-content: space-between; /* Distribuye 80% arriba y 20% abajo */
  height: 80vh; /* Ocupa toda la pantalla */
  width: 100%;
  padding: 30px;
}

/* Sección de respuesta (80% de la altura) */
.respuesta-box {
  display: flex;
  align-items: center; /* Centrar contenido verticalmente */
  justify-content: center; /* Centrar contenido horizontalmente */
  height: 70%;
  width: 100%;
  text-align: center;
  font-size: 24px;
}

/* Sección del chat (20% de la altura) */
.chat-box {
  display: flex;
  align-items: center; /* Centra verticalmente el contenido */
  justify-content: center; /* Centra horizontalmente el contenido */
  height: 36%;
  max-width: 600px; /* Máximo ancho del chat */
  box-shadow: 0px -2px 10px rgba(0, 0, 0, 0.1); /* Sombra superior */
  border-radius: 10px 10px 0 0; /* Bordes redondeados arriba */
  padding: 10px;
}
</style>
