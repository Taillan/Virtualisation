<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header>
    <nav class="navbar navbar-expand navbar-dark bg-dark">
      <a class="navbar-brand" href="#">
        <img src="@/assets/logo.svg" width="30" height="30" class="d-inline-block align-top" alt="">
        Quizz App
      </a>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav">
          <li class="nav-item">
            <RouterLink to="/" class="nav-link">Home</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/admin" class="nav-link">admin</RouterLink>
          </li>
        </ul>
      </div>
    </nav>
  </header>
  <div class="container bg-light pb-4 pt-4">
    <RouterView />
  </div>
</template>

<style>
@import "@/assets/base.css";
@import "@/assets/bootstrap.min.css";
</style>