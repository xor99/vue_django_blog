<template>
  <Container>
    <BaseCard>
      <div class="tags-list">
        <div class="tags-item" v-for="item in results" :key="item.name">
          <h2>{{ item.name }}</h2>
          <ol class="tags-article-list">
            <li
              class="tags-article-item"
              v-for="article in item.tag_articles"
              :key="article.title"
            >
              <router-link
                v-if="article"
                :to="{ name: 'ArticleDetail', params: { id: article.id } }"
              >
                {{ article.title }}
              </router-link>
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
  name: "Tags",
  data() {
    return {
      data: "",
      results: {},
    };
  },
  components: {
    Container,
    BaseCard,
  },
  mounted() {
    axios
      .get("/api/tags/")
      .then(
        (response) => (
          (this.data = response.data), (this.results = response.data)
        )
      );
  },
};
</script>

<style>
.tags-article-item {
  list-style-type: decimal;
  list-style-position: inside;

  padding: 0.5em;
}
</style>