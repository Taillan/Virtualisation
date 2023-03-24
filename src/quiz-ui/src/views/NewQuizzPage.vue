<template>
  <div class="NewQuizzPage">
    <h1 class="text-center pt-4">New Quizz</h1>
    <p>Saisissez votre nom:</p>
    <div class="LoginDiv input-group mb-3 mt-4" v-if="!this.token">
      <input type="Username" class="form-control" placeholder="username" v-model="username" v-on:keyup.enter="launchNewQuiz" />
      <div class="input-group-append">
        <button class="btn btn-primary" @click="launchNewQuiz">GO !</button>
      </div>
    </div>
  </div>
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "NewQuizzPage",
  data() {
    return {
      username: "",
    };
  },
  methods: {
    async created() {
      console.log("Composant NewQuizzPage page 'created'");
    },
    launchNewQuiz() {
      participationStorageService.savePlayerName(this.username);
      console.log("Launch new quiz with", this.username);
      this.$router.push("/questions");
    },
  },
};
</script>

<style>
@media (min-width: 1024px) {
}
</style>
