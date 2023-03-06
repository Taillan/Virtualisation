<template>
  <h1 class="text-center pt-4">Home</h1>
  <router-link to="/start-new-quiz-page" class="btn btn-block btn-primary mt-4">Démarrer le quiz !</router-link>
  <ul class="list-group mt-4">
    <li class="list-group-item mb-0" v-for="scoreEntry in this.registeredScores" v-bind:key="scoreEntry.date">
      {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
    </li>
  </ul>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: [],
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    let tempQuizScores = await quizApiService.getQuizInfo();
    this.registeredScores = tempQuizScores.data.scores;
  },

  methods: {},
};
</script>

<style>
</style> 