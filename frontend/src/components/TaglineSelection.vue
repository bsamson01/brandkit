<template>
  <div class="container mx-auto p-4">
    <h2 class="text-xl font-semibold mb-4 text-center">Choose a Tagline</h2>
    <LoadingSpinner v-if="loading" />

    <div v-else>
      <div class="space-y-3">
        <button
          v-for="(line, idx) in store.taglineOptions"
          :key="idx"
          @click="selectTagline(line)"
          class="w-full border rounded p-3 text-left"
          :class="store.selectedTagline === line ? 'bg-blue-100 border-blue-600' : ''"
        >
          {{ line }}
        </button>
      </div>
      <button
        class="mt-6 w-full bg-blue-600 text-white py-2 rounded disabled:opacity-50"
        :disabled="!store.selectedTagline"
        @click="router.push('/colors')"
      >
        Next
      </button>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import LoadingSpinner from './LoadingSpinner.vue';
import { store } from '../store.js';

const BASE_URL = import.meta.env.VITE_BACKEND_URL || 'http://localhost:8000';
const router = useRouter();
const loading = ref(true);
let intervalId;

function selectTagline(line) {
  store.selectedTagline = line;
}

async function fetchTask() {
  const resp = await fetch(`${BASE_URL}/api/tasks/${store.taglineTaskId}`);
  const data = await resp.json();
  if (data.status === 'completed') {
    store.taglineOptions = data.result;
    loading.value = false;
    clearInterval(intervalId);
  }
}

onMounted(async () => {
  // If user already provided tagline upfront, skip generation
  if (store.business.tagline) {
    store.taglineOptions = [store.business.tagline];
    store.selectedTagline = store.business.tagline;
    loading.value = false;
  } else {
    await fetchTask();
    if (loading.value) {
      intervalId = setInterval(fetchTask, 2000);
    }
  }
});
</script>