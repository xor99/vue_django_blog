<template>
  <div id="app" class="app">
    <div class="header">
      <div class="nav_bar">
        <ul class="nav-bar-card">
          <li><router-link to="/">主页</router-link></li>
          <li><router-link to="/category">归档</router-link></li>
          <li><router-link to="/tags">标签</router-link></li>
        </ul>
      </div>
    </div>
    <div class="main">
      <transition name="fade" mode="out-in">
        <router-view />
      </transition>
    </div>
    <div class="footer">
      <div class="footer-content">
        <p>Power By Vue, Django</p>
      </div>
    </div>
  </div>
</template>

<style>
:root {
  box-sizing: border-box;
  font-family: Arial, Helvetica, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 1em;
}

*,
::before,
::after {
  box-sizing: inherit;
  padding: 0;
  margin: 0;
}

body {
  background-color: #f8f8f8;
}

a {
  color: inherit;
  text-decoration: none;
}

li {
  list-style-type: none;
}

.app {
  height: 100vh;
  width: 100vw;
  max-width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.main {
  flex: 1 0 auto;
}

/* Nav Bar */
.header {
  flex: 0 0 auto;
  margin: 2em 0;
}

.nav_bar {
  font-size: 1.5rem;
  font-weight: 600;
  max-width: max-content;
  padding: 0 1em;
}

.nav-bar-card {
  background-color: #ffffff;
  border-radius: 0.5em;
  font-size: 1rem;

  box-shadow: 5px 5px 10px 10px rgba(0, 0, 0, 2%);
  transition: transform 0.5s, box-shadow 0.3s;
}

.nav-bar-card:hover {
  transform: scale(1.02);
  box-shadow: 2px 2px 5px 5px rgba(0, 0, 0, 8%);
}

.nav_bar ul {
  display: flex;
  justify-content: center;
}

.nav_bar li {
  margin-right: 1em;
  margin-top: 0;
}

.nav_bar li:last-child {
  margin-right: 0;
}

.nav_bar li a {
  display: block;
  padding: 1em;
}

/* Footer */
.footer {
  flex: 0 0 auto;
  padding: 0;
  max-width: max-content;
  margin-top: 2em;
}

.footer-content {
  text-align: center;
}

.footer-content p {
  color: gray;
  padding: 1em;
}

/* Vue Router Transition */
/*进入过渡的结束状态，元素被插入时就生效，在过渡过程完成后移除*/
.fade-enter-active {
  transition: opacity 0.3s;
}
/*进入过渡的开始状态，元素被插入时生效，只应用一帧后立刻删除*/
.fade-enter {
  opacity: 0;
}
/*离开过渡的开始状态，元素被删除时触发，只应用一帧后立刻删除*/
.fade-leave {
  opacity: 1;
}
/*离开过渡的结束状态，元素被删除时生效，离开过渡完成后被删除*/
.fade-leave-active {
  opacity: 0;
  transition: opacity 0.5s;
}
</style>
