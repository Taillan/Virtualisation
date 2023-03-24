<template>
  <div class="AdminPage">
    <h1 class="text-center pt-4">Admin panel</h1>
    <div class="LoginDiv input-group mb-3 mt-4" v-if="!this.token">
      <input type="Password" class="form-control" placeholder="Password" v-model="password" v-on:keyup.enter="login" />
      <div class="input-group-append">
        <button class="btn btn-primary" @click="login">Login</button>
      </div>
    </div>
    <div v-if="wrongpassword" class="alert alert-danger" role="alert">Wrong password</div>

    <div class="AdminModeDiv text-center" v-if="this.token">
      <button class="btn btn-lg btn-primary m-4" @click="deconnexion">Deconnexion</button>
      <br>
      <QList v-if="this.adminMode=='QuestionsList'" @question-selected="questionSelected"/>
      <QEdit v-if="this.adminMode=='QuestionsEdition'" @goBack="this.adminMode='QuestionsList';" :position="questionSelectedPosition"/>
      <QDisplay v-if="this.adminMode=='QuestionAdminDisplay'" @goBack="this.adminMode='QuestionsList';" @goEdit="this.adminMode='QuestionsEdition';" :questionPosition="questionSelectedPosition"/>
    </div>
  </div>
</template>

<script>
import AdminStorageService from "@/services/AdminStorageService";
import AdminApiService from "@/services/AdminApiService";
import QuestionsEdition from "@/components/Admin/QuestionsEdition.vue";
import QuestionAdminDisplay from "@/components/Admin/QuestionAdminDisplay.vue";
import QuestionsList from "@/components/Admin/QuestionsList.vue";

export default {
  name: "AdminPage",
  components: {
    QList: QuestionsList,
    QEdit: QuestionsEdition,
    QDisplay: QuestionAdminDisplay,
  },
  data() {
    return {
      wrongpassword:false,
      password: "",
      token:"",
      adminMode:"QuestionsList",
      questionSelectedPosition:null,
    };
  },
  methods: {
    async created() {
      console.log("Composant AdminPage page 'created'");
    },
    questionSelected(position){
      this.questionSelectedPosition = position;
      this.adminMode='QuestionAdminDisplay';
    }
    ,
    async login(){
      let response 
      try{
      response = await AdminApiService.postLogin(this.password);
      this.token=response.data.token;
      AdminStorageService.saveAdminToken(this.token);
      this.wrongpassword=false;
      }catch(error){
        this.wrongpassword=true;
      }

    },
    deconnexion(){
      console.log("Deconnexion");
      AdminStorageService.clear();
      this.token="";
    },
  },
};
</script>

<style>
</style>
