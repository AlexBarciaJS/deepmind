<script setup lang="ts">
import { ref } from 'vue'
import { useMainStore } from '../store';
import { sendChatMessage } from '../services/apiService';

const store = useMainStore();
defineProps<{ msg: string }>()

const count = ref(0)
const posts = ref<{ id: number; title: string; body: string }[]>([]);
const loading = ref(true);

const handleSendMessage = async () => {
  try {
    const response = await sendChatMessage(store.chatMessage);
    console.log('Message sent:', response);
    // Optionally, you can update the store with the response
    store.messages.push({ id: Date.now(), text: response.answer });
  } catch (error) {
    console.error('Failed to send message');
  }
};
</script>

<template>
  <h1>{{ msg }}</h1>

  <div class="card">
    <p>Chat</p>
    <input type="text" v-model="store.chatMessage" />
    <button class="btn btn-primary" @click="handleSendMessage">Send</button>
    <ul>
      <li v-for="message in store.messages" :key="message.id">
        {{ message.text }}
      </li>
    </ul>
  </div>

  <div class="container mt-4">
    <h2 class="text-primary">Posts</h2>
    <div v-if="loading">Loading...</div>
    <ul v-else class="list-group">
      <li v-for="post in posts" :key="post.id" class="list-group-item">
        <h5>{{ post.title }}</h5>
        <p>{{ post.body }}</p>
      </li>
    </ul>
  </div>
  <p>
    Check out
    <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank"
      >create-vue</a
    >, the official Vue + Vite starter
  </p>
  <p>
    Learn more about IDE Support for Vue in the
    <a
      href="https://vuejs.org/guide/scaling-up/tooling.html#ide-support"
      target="_blank"
      >Vue Docs Scaling up Guide</a
    >.
  </p>
  <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>