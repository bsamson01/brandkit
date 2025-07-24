<template>
  <div class="container mx-auto p-4 flex-1 flex flex-col justify-center">
    <h1 class="text-2xl font-bold mb-4 text-center">BrandKit Builder - Docker Edition</h1>
    <form @submit.prevent="handleSubmit" class="space-y-4 max-w-md mx-auto bg-white p-6 rounded shadow">
      <div>
        <label class="block text-sm font-medium mb-1" for="business_name">Business Name *</label>
        <input
          id="business_name"
          type="text"
          v-model="store.business.business_name"
          class="w-full border rounded p-2"
          required
        />
      </div>
      <div>
        <label class="block text-sm font-medium mb-1" for="industry">Industry *</label>
        <input
          id="industry"
          type="text"
          v-model="store.business.industry"
          class="w-full border rounded p-2"
          required
        />
      </div>
      <div>
        <label class="block text-sm font-medium mb-1" for="tagline">Tagline (optional)</label>
        <input
          id="tagline"
          type="text"
          v-model="store.business.tagline"
          class="w-full border rounded p-2"
        />
      </div>

      <button
        type="submit"
        class="w-full bg-blue-600 text-white py-2 rounded disabled:opacity-50"
        :disabled="loading"
      >
        {{ loading ? 'Loading...' : 'Continue' }}
      </button>

      <p v-if="error" class="text-red-600 text-sm">{{ error }}</p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { store } from '../store.js';

const BASE_URL = import.meta.env.VITE_BACKEND_URL || 'http://localhost:8000';

const router = useRouter();
const loading = ref(false);
const error = ref('');

async function handleSubmit() {
  error.value = '';
  loading.value = true;
  try {
    const resp = await fetch(`${BASE_URL}/api/taglines`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(store.business),
    });
    const data = await resp.json();
    if (!resp.ok) {
      throw new Error(data.detail || 'Failed to request tagline');
    }
    store.taglineTaskId = data.task_id;
    router.push('/taglines');
  } catch (e) {
    error.value = e.message;
  } finally {
    loading.value = false;
  }
}
</script>