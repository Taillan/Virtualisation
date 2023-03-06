<template>
  <h1>Question Edition page</h1>
    <QForm 
      actionForm="Edit Question"
      :position="this.position"
      @form-completed="editQuestion"/>
    <button class="btn btn-primary" @click="$emit('goBack')">
      Discard changes
    </button>
</template>

<script>
import AdminStorageService from "@/services/AdminStorageService";
import AdminApiService from "@/services/AdminApiService";
import QuestionForm from "@/components/Admin/QuestionForm.vue";

export default {
  name: "QuestionEdition",
  emits: ['goBack'],
  props: {
    position: Number,
  },
  components: {
    QForm: QuestionForm,
  },

  data() {
    return {
      oldPosition:null,
      currentQuestion: {},
    };
  },

  async created() {
    this.oldPosition = this.position;
    console.log("Composant QuestionEdition 'created'");
  },

  methods: {
    async editQuestion(text,title,image,pose,textA,answerA,textB,answerB,textC,answerC,textD,answerD){
      console.log("pose :",pose);
        await AdminApiService.editQuestion(this.oldPosition,text,title,"",parseInt(pose),textA,answerA,textB,answerB,textC,answerC,textD,answerD,AdminStorageService.getAdminToken());
        this.$emit('goBack');
    },
  }
};
</script>

<style>
</style> 