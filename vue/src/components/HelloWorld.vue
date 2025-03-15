<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useMainStore } from '../store';
import { fetchPosts } from '../services/apiService';


const store = useMainStore();
defineProps<{ msg: string }>()

const count = ref(0)
const posts = ref<{ id: number; title: string; body: string }[]>([]);
const loading = ref(true);

onMounted(async () => {
  try {
    posts.value = await fetchPosts();
  } catch (error) {
    console.error('Failed to fetch posts');
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <h1>{{ msg }}</h1>

  <div class="card">
    <button type="button" @click="count++">count is {{ count }}</button>
    <p>
      Edit
      <code>components/HelloWorld.vue</code> to test HMR
    </p>
    <p>Counter: {{ store.counter }}</p>
    <button class="btn btn-primary" @click="store.increment">Increment</button>
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
