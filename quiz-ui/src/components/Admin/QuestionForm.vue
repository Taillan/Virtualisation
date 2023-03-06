<template>
  <div class="QuestionForm">

    <div class="input-group mb-3">
      <div class="input-group-prepend">
        <span class="input-group-text" id="title">title</span>
      </div>
      <input type="text" class="form-control" aria-label="title" aria-describedby="title" v-model="title">
    </div>

    <div class="input-group mb-3">
      <div class="input-group-prepend">
        <span class="input-group-text" id="position">position</span>
      </div>
      <input @keypress="onlyNumber" type="number" class="form-control" aria-label="position" aria-describedby="position" v-model="pose">
    </div>

    <div class="input-group mb-3">
      <div class="input-group-prepend">
        <span class="input-group-text" id="text">text</span>
      </div>
      <input type="text" class="form-control" aria-label="text" aria-describedby="text" v-model="text">
    </div>

    <div class="input-group mb-3">
      <div class="input-group-prepend">
        <span class="input-group-text" id="AnswerA">Answer A</span>
      </div>
      <input type="text" class="form-control" aria-label="AnswerA" aria-describedby="AnswerA" v-model="textA">
    </div>

    <div class="input-group mb-3">
      <div class="input-group-prepend">
        <span class="input-group-text" id="AnswerB">Answer B</span>
      </div>
      <input type="text" class="form-control" aria-label="AnswerB" aria-describedby="AnswerB" v-model="textB">
    </div>

    <div class="input-group mb-3">
      <div class="input-group-prepend">
        <span class="input-group-text" id="AnswerC">Answer C</span>
      </div>
      <input type="text" class="form-control" aria-label="AnswerC" aria-describedby="AnswerC" v-model="textC">
    </div>

    <div class="input-group mb-3">
      <div class="input-group-prepend">
        <span class="input-group-text" id="AnswerD">Answer D</span>
      </div>
      <input type="text" class="form-control" aria-label="AnswerD" aria-describedby="AnswerD" v-model="textD">
    </div>

    <div class="input-group mb-3">
      <span class="input-group-text mr-2">Is A Correct</span>
      <input type="radio" class="form-check" id="one" value="A" :checked="answerA" v-model="picked" @click="answerA=true;answerB=false;answerC=false;answerD=false">
    </div>

    <div class="input-group mb-3">
      <span class="input-group-text mr-2">Is B Correct</span>
      <input type="radio" id="one" value="B" :checked="answerB" v-model="picked" @click="answerA=false;answerB=true;answerC=false;answerD=false">
    </div>

    <div class="input-group mb-3">
      <span class="input-group-text mr-2">Is C Correct</span>
      <input type="radio" id="one" value="C" :checked="answerC" v-model="picked" @click="answerA=false;answerB=false;answerC=true;answerD=false">
    </div>

    <div class="input-group mb-3">
      <span class="input-group-text mr-2">Is D Correct</span>
      <input type="radio" id="one" value="D" :checked="answerD" v-model="picked" @click="answerA=false;answerB=false;answerC=false;answerD=true">
    </div>  
    
    <ImageUpload @file-change="imageChange"/> 
    <img v-if="this.image" :src="this.image" style="max-height: 35rem;"/>
    <br class="mb-4"/>
    <button class="btn btn-primary mb-4" @click="$emit('form-completed', this.text,this.title,this.image,this.pose,this.textA,this.answerA,this.textB,this.answerB,this.textC,this.answerC,this.textD,this.answerD)">{{actionForm}}</button>

  </div>
</template>

<script>
import ImageUpload from "@/components/ImageUpload.vue";
import quizApiService from "@/services/QuizApiService";

export default {
  name: "QuestionForm",
  emits: ["form-completed"],
  props: {
    actionForm: String,
    position:Number
  },
  components: {
    ImageUpload: ImageUpload,
  },
  data() {
    return {
      picked:"",
      pose:null,
      answerChoice:"",
      title:"",
      textA:"",
      textB:"",
      textC:"",
      textD:"",
      text:"",
      image:"",
      answerA:false,
      answerB:false,
      answerC:false,
      answerD:false,
      showForm:false,
      questionList: [],
      question: {},
    };
  },
  async created() {
    console.log("Composant QuestionForm page 'created'");
    this.pose = this.position;
    if(this.position){
     let tempQuestion = await quizApiService.getQuestionByPosition(this.position);
      this.question = tempQuestion.data;
      this.title = this.question.title;
      this.textA = this.question.possibleAnswers[0].text;
      this.textB = this.question.possibleAnswers[1].text;
      this.textC = this.question.possibleAnswers[2].text;
      this.textD = this.question.possibleAnswers[3].text;
      this.text = this.question.text;
      this.image = this.question.image;
      this.answerA = this.question.possibleAnswers[0].isCorrect;
      this.answerB = this.question.possibleAnswers[1].isCorrect;
      this.answerC = this.question.possibleAnswers[2].isCorrect;
      this.answerD = this.question.possibleAnswers[3].isCorrect;
    }
  },

  methods: {
    imageChange(dataUrl){
      if(dataUrl)this.image=dataUrl;
      else{this.image="";}
      console.log(dataUrl," ",this.image);
    },
    onlyNumber ($event) {
      let keyCode = ($event.keyCode ? $event.keyCode : $event.which);
      if ((keyCode < 48 || keyCode > 57) && keyCode !== 46) { // 46 is dot
          $event.preventDefault();
      }
    }
  },
};
</script>

<style>
.QuestionForm {
  flex-wrap: wrap;
  flex-direction: column  ;
}
</style> 