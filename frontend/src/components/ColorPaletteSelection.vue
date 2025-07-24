<template>
  <div class="container mx-auto p-4">
    <h2 class="text-xl font-semibold mb-4 text-center">Pick a Color Palette</h2>
    <LoadingSpinner v-if="loading" />

    <div v-else>
      <div class="grid gap-4 grid-cols-1 sm:grid-cols-2">
        <div
          v-for="(palette, idx) in palettes"
          :key="idx"
          @click="selectPalette(palette)"
          class="border rounded p-3 cursor-pointer flex gap-1"
          :class="paletteSelected(palette) ? 'border-blue-600' : ''"
        >
          <div
            v-for="(color, cidx) in palette"
            :key="cidx"
            :style="{ background: color }"
            class="flex-1 h-8 rounded"
          ></div>
        </div>
      </div>
      <button
        class="mt-6 w-full bg-blue-600 text-white py-2 rounded disabled:opacity-50"
        :disabled="!store.selectedPalette.length"
        @click="router.push('/logos')"
      >
        Next
      </button>
    </div>
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
const palettes = ref([]);

function selectPalette(palette) {
  store.selectedPalette = palette;
}

function paletteSelected(palette) {
  return JSON.stringify(store.selectedPalette) === JSON.stringify(palette);
}

onMounted(async () => {
  const resp = await fetch(`${BASE_URL}/api/color-palettes`);
  const data = await resp.json();
  palettes.value = data.palettes;
  loading.value = false;
});
</script>