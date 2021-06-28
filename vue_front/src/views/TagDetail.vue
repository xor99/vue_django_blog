<template>
  <Container>
    <BaseCard>
      <div v-if="tag_data.id">
        <h2>{{ tag_data.name }}</h2>
        <h4 v-if="tag_data.tag_articles.length == 0">该标签下暂无内容</h4>
        <ol class="tags-detail-list">
          <li
            class="tags-detail-item"
            v-for="(article, index) in tag_data.tag_articles"
            :key="index"
          >
            <router-link
              :to="{ name: 'ArticleDetail', params: { id: article.id } }"
              >{{ article.title }}</router-link
            >
          </li>
        </ol>
      </div>
    </BaseCard>
  </Container>
</template>

<script>
import axios from "axios";

import Container from "@/components/container.vue";
import BaseCard from "@/components/card/base_card.vue";

export default {
  name: "TagDetail",
  data() {
    return {
      tag_data: {},
    };
  },
  components: {
    Container,
    BaseCard,
  },
  mounted() {
    axios
      .get("/api/tags/" + this.$route.params.id)
      .then((response) => (this.tag_data = response.data));
  },
};
</script>

<style>
.tags-detail-item {
  list-style-type: decimal;
  list-style-position: inside;

  padding: 0.5em;
}
</style>