<template>
  <Container>
    <BaseCard>
      <div class="category-list" v-if="results.id">
        <h2>{{ results.title }}</h2>
        <div class="category-item">
          <ol class="category-article-list">
            <li
              class="category-article-item"
              v-for="article in results.category_articles"
              :key="article.title"
            >
              <router-link
                :to="{ name: 'ArticleDetail', params: { id: article.id } }"
                >{{ article.title }}</router-link
              >
            </li>
          </ol>
        </div>
      </div>
    </BaseCard>
  </Container>
</template>

<script>
import axios from "axios";

import Container from "@/components/container.vue";
import BaseCard from "@/components/card/base_card.vue";
export default {
  name: "CategoryDetail",
  components: {
    Container,
    BaseCard,
  },
  data() {
    return {
      results: {},
    };
  },
  mounted() {
    axios
      .get("/api/category/" + this.$route.params.id)
      .then((response) => (this.results = response.data));
  },
};
</script>

<style>
</style>