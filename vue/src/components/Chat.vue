<script setup lang="ts">
import { ref } from 'vue'
import { useMainStore } from '../store';
import { sendChatMessage } from '../services/apiService';

const store = useMainStore();
defineProps<{ msg: string }>()

const loading = ref(false);

const handleSendMessage = async () => {
  loading.value = true;
  try {
    const response = await sendChatMessage(store.chatMessage);
    console.log('Message sent:', response);
    // Optionally, you can update the store with the response
    store.messages.push({ id: Date.now(), question: store.chatMessage, response: response });
    store.chatMessage = '';
  } catch (error) {
    console.error('Failed to send message');
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <h1>{{ msg }}</h1>

  <div class="card">
    <ul>
      <li v-for="message in store.messages" :key="message.id">
        <div calss="chat">
          <div class="question">
            <span>
              {{ message.question }}
            </span>
          </div>
          <br>
          <div  class="response">
            <span>
              {{ message.response }}
            </span>
          </div>
        </div>
      </li>
    </ul>
    <input type="text" v-model="store.chatMessage" :disabled="loading" />
    <button class="btn btn-primary" @click="handleSendMessage" :disabled="loading">
      {{ loading ? 'Sending...' : 'Send' }}
    </button>
  </div>
</template>
<style scoped>
.card {
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.chat {
  display: flex;
  justify-content: space-between;
}

.question {
  font-weight: bold;
  text-align: left;
}

.response {
  font-style: italic;
  text-align: right;
}
</style>