<template>
  <div class="container">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "Container",
};
</script>

<style>
.container {
  display: flex;
  justify-content: center;

  padding-top: 0;
}
</style>