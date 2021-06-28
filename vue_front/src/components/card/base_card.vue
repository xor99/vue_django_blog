<template>
  <div class="base-card">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "BaseCard",
};
</script>

<style>
/* Base Card */
.base-card {
  --card-color: #ffffff;
}

.base-card {
  width: 95vw;
  padding: 1em;
  margin-bottom: 3em;

  background-color: var(--card-color);
  border-radius: 0.5em;
  font-size: 1rem;
  box-shadow: 5px 5px 10px 10px rgba(0, 0, 0, 2%);
}

@media screen and (min-width: 1200px) {
  .base-card {
    min-width: 800px;
    max-width: 800px;
  }
}
</style>