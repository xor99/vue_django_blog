<template>
  <div class="article-card">
    <div class="article-title">
      <h2>
        <router-link :to="{ name: 'ArticleDetail', params: { id: article.id } }"
          >{{ article.title }}
        </router-link>
      </h2>
    </div>
    <div class="article-content" v-html="article.body_html"></div>
    <div class="article-details">
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
          {{ article.category.title }}</router-link
        >
      </div>
      <div class="article-date">
        <p>
          <font-awesome-icon icon="calendar-alt" />
          {{ "创建时间 " + datetime_format(article.created) }}
        </p>
      </div>
      <div class="article-read">
        <router-link
          :to="{ name: 'ArticleDetail', params: { id: article.id } }"
        >
          阅读全文
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Article_Card",
  props: ["article"],
  methods: {
    datetime_format: function (datetime) {
      const date = new Date(datetime);
      return date.toLocaleDateString();
    },
  },
};
</script>

<style>
/* Article Card */
.article-card {
  --card-color: #ffffff;
}

.article-card {
  width: 95vw;
  padding: 1em;
  margin-bottom: 2em;

  background-color: var(--card-color);
  border-radius: 0.5em;
  font-size: 1rem;

  box-shadow: 5px 5px 10px 10px rgba(0, 0, 0, 2%);
  transition: transform 0.5s, box-shadow 0.3s;
}

.article-content {
  margin-bottom: 1em;
  padding-bottom: 1em;
  border-bottom: 2px solid gray;
}

@media screen and (min-width: 1200px) {
  .article-card {
    min-width: 800px;
    max-width: 800px;
    margin-bottom: 3em;
  }
}

.article-card:hover {
  transform: scale(1.02);
  box-shadow: 2px 2px 5px 5px rgba(0, 0, 0, 8%);
}

.article-title {
  margin-top: 1.5em;
  margin-bottom: 1em;
}

.article-details {
  margin-bottom: 0.5em;
}

.article-tag-list {
  margin-bottom: 0.5em;
  display: inline-block;
}

.article-tag-item {
  display: inline-block;
  margin-right: 1em;
}

.article-category {
  margin-bottom: 0.5em;
  display: inline-block;
}

.article-tag-item a,
.article-category a {
  padding: 0.5em;
  display: block;
}

/* Article Content */
.article-content * {
  margin-bottom: 0.5em;
}

.article-content ul,
.article-content ol {
  padding: 1em;
}

.article-content p {
  padding: 0.5em;
}

.article-content ul li {
  list-style-type: disc;
}

.article-content ol li {
  list-style-type: decimal;
}

.article-content img {
  width: 100%;
  height: 100%;
  max-width: 100%;
  max-height: 100%;

  background-size: cover;
  background-position: center;
}

.article-read {
  margin: 0 auto;
  margin-top: 0.5em;
  max-width: max-content;
}

.article-read a:hover {
  border-bottom: 1px solid black;
}
</style>