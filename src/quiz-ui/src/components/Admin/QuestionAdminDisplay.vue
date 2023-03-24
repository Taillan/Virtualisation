<template>
  <div class="QuestionAdminDisplay text-center">
    <div class="btn-group mb-2" role="group" aria-label="Basic example">
      <button class="btn btn-primary" @click="$emit('goBack')">
        Back
      </button>
      <button class="btn btn-primary" @click="$emit('goEdit')">
        Edit
      </button>
      <button class="btn btn-primary" @click="Delete">
        Delete
      </button>
    </div>
    <QDisplay
    :question="currentQuestion"
    :admin="true"></QDisplay>
    

  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import AdminApiService from "@/services/AdminApiService";
import AdminStorageService from "@/services/AdminStorageService";
import QuestionDisplay from "@/components/QuestionDisplay.vue";

export default {
  name: "QuestionAdminDisplay",
  emits: ['goBack','goEdit'],
  components: {
    QDisplay: QuestionDisplay,
  },
  props: {
    questionPosition:Number
  },
  data() {
    return {
      currentQuestion: {},
    };
  },
  async created() {
    console.log("Composant QuestionAdminDisplay page 'created'");
    let tempQuestion = await quizApiService.getQuestionByPosition(this.questionPosition);
    this.currentQuestion = tempQuestion.data;
    console.log(this.currentQuestion );
  },

  methods: {
    Delete(){
      this.$emit('goBack');
      AdminApiService.deleteQuestion(this.questionPosition,AdminStorageService.getAdminToken());
    }
  },
};
</script>

<style>
.QuestionAdminDisplay {
  flex-wrap: wrap;
  flex-direction: column  ;
}
</style> 