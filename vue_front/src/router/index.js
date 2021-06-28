import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Category from '@/views/Category.vue'
import CategoryDetail from '@/views/CategoryDetail.vue';
import ArticleDetail from '@/views/ArticleDetail.vue'
import Tags from '@/views/Tags.vue'
import TagDetail from '@/views/TagDetail.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/article/:id',
    name: 'ArticleDetail',
    component: ArticleDetail
  },
  {
    path: '/category',
    name: 'Category',
    component: Category
  },
  {
    path: '/category/:id',
    name: 'CategoryDetail',
    component: CategoryDetail
  },
  {
    path: '/tags',
    name: 'Tag',
    component: Tags
  },
  {
    path: '/tags/:id',
    name: 'TagDetail',
    component: TagDetail,
  }
]

const router = new VueRouter({
  mode: 'history',
  routes,
})

export default router
