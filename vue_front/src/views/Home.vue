<template>
  <Container v-if="info.results">
    <div class="article-list">
      <ArticleCard
        v-for="(article, index) in info.results"
        :key="index"
        :article="article"
      ></ArticleCard>
      <div class="page-control">
        <div
          class="page_previous page-button"
          v-if="is_page_exists('previous')"
        >
          <router-link
            :to="{
              name: 'Home',
              query: { page: get_page_param('previous') },
            }"
            >上一页</router-link
          >
        </div>
        <div class="page_next page-button" v-if="is_page_exists('next')">
          <router-link
            :to="{ name: 'Home', query: { page: get_page_param('next') } }"
            >下一页</router-link
          >
        </div>
      </div>
    </div>
    <div class="sider-bar">
      <AuthorCard :author_config="this.config"></AuthorCard>
      <TagsCard></TagsCard>
    </div>
  </Container>
</template>

<script>
import axios from "axios";

import Container from "@/components/container.vue";
import ArticleCard from "@/components/card/article_card.vue";
import AuthorCard from "@/components/card/author_card.vue";
import TagsCard from "@/components/card/tags_card.vue";

var config = {
  author_name: "夏日繁星",
};

export default {
  name: "Home",
  data() {
    return {
      config: config,
      info: {},
    };
  },
  components: {
    Container,
    ArticleCard,
    AuthorCard,
    TagsCard,
  },
  methods: {
    is_page_exists(direction) {
      if (direction == "next") {
        return this.info.next !== null;
      }
      return this.info.previous !== null;
    },
    get_page_param(direction) {
      try {
        let url_string;
        switch (direction) {
          case "next":
            url_string = this.info.next;
            break;
          case "previous":
            url_string = this.info.previous;
            break;
          default:
            return this.$route.query.page;
        }

        const url = new URL(url_string);
        return url.searchParams.get("page");
      } catch (err) {
        return;
      }
    },
    get_article() {
      try {
        let url_string = "/api/article";
        const page_index = Number(this.$route.query.page);
        if (!isNaN(page_index) && page_index !== 0) {
          url_string = url_string + "/?page=" + page_index;
        }

        axios.get(url_string).then((response) => (this.info = response.data));
      } catch (err) {
        return;
      }
    },
  },
  mounted() {
    this.get_article();
  },
  watch: {
    $route() {
      this.get_article();
    },
  },
};
</script>

<style>
/* Side Bar */
.sider-bar {
  display: none;
}

@media screen and (min-width: 1200px) {
  .sider-bar {
    display: block;
    margin-left: 2em;
    height: max-content;
  }
}

.page-control {
  margin: 0 auto;
  max-width: max-content;
}

.page-button {
  background: #ffffff;
  border-radius: 0.5em;
  display: inline-block;
  box-shadow: 5px 5px 10px 10px rgba(0, 0, 0, 2%);
  transition: transform 0.5s, box-shadow 0.3s;
}

.page-button:hover {
  transform: scale(1.02);
  box-shadow: 2px 2px 5px 5px rgba(0, 0, 0, 8%);
}

.page-button a {
  display: block;
  padding: 1em;
}

.page-button + .page-button {
  margin-left: 1em;
}
</style>