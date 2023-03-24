<template>
  <div class="text-center">
    <h1 class="mb-4">Questions list</h1>
      <button class="btn btn-primary mb-4" @click="this.showForm = !this.showForm;this.showList = !this.showList" >Add New Question</button>
      <div class="AddQuestionDiv" v-if="this.showForm" >
        <QForm 
        actionForm="Send Question"
      @form-completed="addNewQuestion"/>
      </div>
      
      <div class="list-group" v-if="this.showList">
        <div v-for="question in this.questionList" v-bind:key="question.position" >
          <router-link class="list-group-item list-group-item-action" to="" @click="$emit('question-selected', question.position)" >
            {{ question.position }} - {{ question.title }}
          </router-link>
        </div>
      </div>
  </div>
</template>

<script>
import AdminApiService from "@/services/AdminApiService";
import AdminStorageService from "@/services/AdminStorageService";
import QuestionForm from "@/components/Admin/QuestionForm.vue";

export default {
  name: "QuestionList",
  emits: ["question-selected"],
  components: {
    QForm: QuestionForm,
  },
  data() {
    return {
      showForm:false,
      showList:true,
      questionList: [],
    };
  },
  async created() {
    console.log("Composant Admin page 'created'");
    this.updateQuestionList();
  },

  methods: {
    async addNewQuestion(text,title,image,position,textA,answerA,textB,answerB,textC,answerC,textD,answerD){
      await AdminApiService.postAddQuestion(text,title,image,parseInt(position),textA,answerA,textB,answerB,textC,answerC,textD,answerD,AdminStorageService.getAdminToken());
      this.showForm = false;
      this.showList = true;
      this.updateQuestionList();
    },
    async updateQuestionList(){
      let response = await AdminApiService.getAllQuestion();
      this.questionList = response.data.sort(function(a, b) {return  a.position -b.position;});
    }
  },
};
</script>

<style>
</style> 