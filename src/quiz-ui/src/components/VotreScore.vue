<template>
  GG {{currentPlayer}}, tu as fini avec un score de {{finalScore}}
  Tu es {{scoreClassement}} sur {{numberOfParticipant}}
  <router-link to="/">Retour a l'accueil</router-link><div v-for="scoreEntry in this.registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "QuestionsManager",
  components: {
  },

  data() {
    return {
      currentPlayer :"",
      numberOfParticipant:0,
      finalScore:0,
      scoreBoard:[],
      scoreClassement:0,
      registeredScores: [],
    };
  },

  async created() {
    console.log("Composant VotreScore 'created'");
    this.currentPlayer = participationStorageService.getPlayerName();
    this.finalScore = parseInt(participationStorageService.getParticipationScore());

    let tempQuizzInfo = await  quizApiService.getQuizInfo();

    let tempBoard = [];
    tempQuizzInfo.data.scores.forEach(function(participant){
      tempBoard.push(participant.score);
    })


    this.scoreBoard = tempBoard;
    this.numberOfParticipant = this.scoreBoard.length;
    
    this.scoreBoard.sort(function(a, b) {return a - b;});

    console.log(this.scoreBoard);
    this.scoreBoard.forEach((el, index) => {
      if (el <= this.finalScore){
        this.scoreClassement =  this.numberOfParticipant - index ;
        return;
      } 
    })

    
    let tempQuizScores = await quizApiService.getQuizInfo();
    this.registeredScores = tempQuizScores.data.scores.slice(0, 5);

  },
  unmounted(){
    participationStorageService.clear()
  },
};
</script>

<style>
</style> 