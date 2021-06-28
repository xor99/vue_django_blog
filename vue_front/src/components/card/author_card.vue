<template>
  <div class="author-card">
    <div class="author-img">
      <img src="../../assets/author_img.jpg" alt="作者头像" />
    </div>
    <div class="author-meta">
      <div class="author-name">{{ user_name }}</div>
      <div class="author-social-tags">
        <ul>
          <li>
            <a href="" @click="get_github">
              <font-awesome-icon :icon="['fab', 'github']" size="2x" />
            </a>
          </li>
          <li>
            <a :href="email">
              <font-awesome-icon :icon="['fas', 'at']" size="2x"
            /></a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

var config = {
  github_url: "www.github.com/xor99", // Github地址
  email: "1737451253@qq.com", // 邮件地址
};

export default {
  name: "author_card",
  props: ["author_config"],
  data() {
    return {
      user: {},
      config: config,
    };
  },
  methods: {
    get_github() {
      window.open("https://" + this.config.github_url);
    },
  },
  computed: {
    user_name() {
      return this.user.first_name + this.user.last_name;
    },
    email() {
      return "mailto:" + this.config.email;
    },
  },
  mounted() {
    axios.get("/api/user").then((response) => (this.user = response.data[0]));
  },
};
</script>

<style>
/* Author Card */
.author-card {
  --card-color: #ffffff;
}

.author-card {
  width: 15vw;
  padding: 1em;
  margin-bottom: 1em;
  background-color: var(--card-color);
  border-radius: 0.5em;
  font-size: 1rem;

  box-shadow: 5px 5px 10px 10px rgba(0, 0, 0, 2%);
  transition: transform 0.5s, box-shadow 0.3s;
}

.author-card:hover {
  transform: scale(1.02);
  box-shadow: 2px 2px 5px 5px rgba(0, 0, 0, 8%);
}

.author-meta {
  display: flex;
  flex-direction: column;
  align-items: center;

  margin-bottom: 1em;
}

.author-img {
  padding-bottom: 100%;
  position: relative;

  margin-bottom: 1em;
}

.author-card img {
  position: absolute;
  width: 100%;
  height: 100%;
  border-radius: 50%;
}

.author-name {
  font-size: 1.3rem;
  font-weight: 600;
  padding: 0.5em 0;
  margin-bottom: 1em;
}

.author-social-tags ul {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

.author-social-tags a {
  display: block;
  padding: 0 0.5em;
}

@media screen and (max-width: 1800px) {
  .author-card {
    width: 20vw;
  }
}
</style>