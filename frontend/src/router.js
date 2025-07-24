import { createRouter, createWebHistory } from 'vue-router';
import BusinessForm from './components/BusinessForm.vue';
import TaglineSelection from './components/TaglineSelection.vue';
import ColorPaletteSelection from './components/ColorPaletteSelection.vue';
import LogoPreview from './components/LogoPreview.vue';

const routes = [
  { path: '/', component: BusinessForm },
  { path: '/taglines', component: TaglineSelection },
  { path: '/colors', component: ColorPaletteSelection },
  { path: '/logos', component: LogoPreview },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;