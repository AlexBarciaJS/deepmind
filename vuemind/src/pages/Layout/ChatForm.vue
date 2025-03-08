<template>
  <form>
    <md-card>
      <md-card-content>
        <div class="md-layout">
          <div class="md-layout-item md-size-100">
            <md-field maxlength="5">
              <label>Haz una pregunta</label>
              <md-textarea v-model="message"></md-textarea>
            </md-field>
          </div>
          <div class="md-layout-item md-size-100 text-right">
            <md-button class="md-button md-round md-just-icon md-twitter" @click="sendQuestion">
              <i class="fa fa-paper-plane" aria-hidden="true"></i>
            </md-button>
          </div>
        </div>
      </md-card-content>
    </md-card>
  </form>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      message: "",   // Stores the text entered in the textarea
      response: ""   // Stores the API response
    };
  },
  methods: {
    async sendQuestion() {
      if (!this.message.trim()) {
        alert("Please enter a question before sending.");
        return;
      }

      try {
        // Build the URL with the entered message
        const url = `http://127.0.0.1:8000/brain/preguntar/?query=${encodeURIComponent(this.message)}`;
        
        // Make the GET request to the API
        const apiResponse = await axios.get(url);

        // Store the API response in the state variable
        this.response = apiResponse.data.respuesta;
      } catch (error) {
        console.error("Error sending the request:", error);
        this.response = "An error occurred while fetching the response.";
      }
    }
  }
};
</script>
<style></style>
