<template>
  <div class="container mx-auto p-4">
    <h2 class="text-xl font-semibold mb-4 text-center">Your Logos</h2>
    <LoadingSpinner v-if="loading" />

    <div v-else class="grid gap-4 grid-cols-1 sm:grid-cols-3">
      <img
        v-for="(url, idx) in store.logos"
        :key="idx"
        :src="url"
        :alt="'Logo ' + (idx + 1)"
        class="w-full rounded shadow"
      />
    </div>

    <button
      class="mt-6 w-full bg-gray-600 text-white py-2 rounded"
      @click="router.push('/')"
    >
      Start Over
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import LoadingSpinner from './LoadingSpinner.vue';
import { store } from '../store.js';

const BASE_URL = import.meta.env.VITE_BACKEND_URL || 'http://localhost:8000';
const router = useRouter();
const loading = ref(true);
let intervalId;

async function fetchTask(taskId) {
  const resp = await fetch(`${BASE_URL}/api/tasks/${taskId}`);
  const data = await resp.json();
  if (data.status === 'completed') {
    store.logos = data.result;
    loading.value = false;
    clearInterval(intervalId);
  }
}

onMounted(async () => {
  const resp = await fetch(`${BASE_URL}/api/logos`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      business: store.business,
      tagline_selection: { tagline: store.selectedTagline },
      palette_selection: { palette: store.selectedPalette },
    }),
  });
  const data = await resp.json();
  if (!resp.ok) {
    console.error(data);
    loading.value = false;
    return;
  }
  await fetchTask(data.task_id);
  if (loading.value) {
    intervalId = setInterval(() => fetchTask(data.task_id), 2000);
  }
});
</script>