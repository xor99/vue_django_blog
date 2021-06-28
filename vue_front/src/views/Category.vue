<template>
  <Container>
    <BaseCard>
      <div class="category-list">
        <div class="category-item" v-for="item in results" :key="item.title">
          <h2 class="category-title">{{ item.title }}</h2>
          <ol class="category-article-list">
            <li
              class="category-article-item"
              v-for="article in item.category_articles"
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
  name: "Category",
  data() {
    return {
      data: "",
      results: "",
    };
  },
  components: {
    Container,
    BaseCard,
  },
  mounted() {
    axios
      .get("/api/category")
      .then(
        (response) => (
          (this.data = response.data), (this.results = response.data)
        )
      );
  },
};
</script>

<style>
.category-article-item {
  list-style-type: decimal;
  list-style-position: inside;

  padding: 0.5em;
}
</style>