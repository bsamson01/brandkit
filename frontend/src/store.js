import { reactive } from 'vue';

export const store = reactive({
  business: {
    business_name: '',
    industry: '',
    tagline: '',
  },
  taglineTaskId: '',
  taglineOptions: [],
  selectedTagline: '',
  selectedPalette: [],
  logos: [],
});