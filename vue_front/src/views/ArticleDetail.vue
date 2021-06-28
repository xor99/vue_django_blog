<template>
  <BaseCard>
    <div class="article-detail-card" v-if="article.id">
      <div class="article-title">
        <h2>
          <router-link
            :to="{ name: 'ArticleDetail', params: { id: article.id } }"
            >{{ article.title }}
          </router-link>
        </h2>
      </div>
      <div class="article-date">
        <p>{{ "创建时间 " + datetime_format(article.created) }}</p>
      </div>
      <div class="article-content" v-html="article.body_html"></div>
      <div class="article-tag-list" v-if="article.tags">
        <div
          class="article-tag-item"
          v-for="(tag, index) in article.tags"
          :key="index"
        >
          <router-link :to="{ name: 'TagDetail', params: { id: tag.id } }">
            <font-awesome-icon icon="tag" />
            {{ tag.name }}
          </router-link>
        </div>
      </div>
      <div class="article-category" v-if="article.category">
        <router-link
          :to="{ name: 'CategoryDetail', params: { id: article.category.id } }"
        >
          <font-awesome-icon icon="archive" />
          {{ article.category.title }}
        </router-link>
      </div>
    </div>
  </BaseCard>
</template>

<script>
import axios from "axios";

import BaseCard from "@/components/card/base_card.vue";

export default {
  name: "Article",
  data: function () {
    return {
      article: {},
    };
  },
  components: {
    BaseCard,
  },
  methods: {
    datetime_format: function (datetime) {
      const date = new Date(datetime);
      return date.toLocaleDateString();
    },
  },
  mounted() {
    axios
      .get("/api/article/" + this.$route.params.id)
      .then((response) => (this.article = response.data));
  },
};
</script>

<style>
/* Article Detail */
.article-detail-card > * {
  margin-bottom: 1em;
}

.article-detail-card .article-tag-list {
  padding: 0.5em 0;
  margin-bottom: 0.5em;
}

.article-detail-card .article-tag-item {
  display: inline-block;
  margin-right: 1em;
}

/* Article Content */
.article-detail-card .article-content * {
  margin-bottom: 0.5em;
}

.article-detail-card .article-content img {
  width: 100%;
  height: 100%;
  max-width: 100%;
  max-height: 100%;

  background-size: cover;
  background-position: center;

  border-radius: 0.5em;
}
</style>