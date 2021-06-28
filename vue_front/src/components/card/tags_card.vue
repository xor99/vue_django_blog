<template>
  <div class="tags-card" v-if="results">
    <h2 class="tags-card-title">标签</h2>
    <ul class="tags-card-list">
      <li v-for="(tag, index) in results" :key="index">
        <router-link :to="{ name: 'TagDetail', params: { id: tag.id } }">
          {{ tag.name }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "tags_card",
  data() {
    return {
      results: {},
    };
  },
  mounted() {
    axios.get("/api/tags").then((response) => {
      this.results = response.data;
    });
  },
};
</script>

<style>
/* Tags Card */
.tags-card {
  --card-color: #ffffff;
}

.tags-card {
  width: 15vw;
  padding: 1em;

  background-color: var(--card-color);
  border-radius: 0.5em;
  font-size: 1rem;

  box-shadow: 5px 5px 10px 10px rgba(0, 0, 0, 2%);
  transition: transform 0.5s, box-shadow 0.3s;
}

.tags-card:hover {
  transform: scale(1.02);
  box-shadow: 2px 2px 5px 5px rgba(0, 0, 0, 8%);
}

.tags-card-title {
  margin-bottom: 1em;
  text-align: center;
}

.tags-card-list {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

.tags-card-list a {
  display: block;
  padding: 1em;
}

@media screen and (max-width: 1800px) {
  .tags-card {
    width: 20vw;
  }
}
</style>