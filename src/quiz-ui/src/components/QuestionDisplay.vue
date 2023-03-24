<template>
  <div class="card text-center mx-auto" style="width: 50rem;">
    <img v-if="question.image" :src="question.image" class="card-img-top" style="max-height: 35rem;" >
    <div class="card-body">
      <h5 class="card-title">{{ question.title }}</h5>
      <p class="card-text">{{ question.text }}</p>
      <div v-if="!this.admin" class="btn-group" style="flex-wrap: wrap;" role="group">
        <div v-for="(answerEntry, index) in this.question.possibleAnswers" v-bind:key="answerEntry.text">
          <button class="btn btn-primary mr-2 mb-1" @click="$emit('answer-selected', index+1,answerEntry.isCorrect)">
            {{ answerEntry.text }}
          </button>
        </div>
      </div>

      <ul  v-if="this.admin" class="list-group">
        <div v-for="(answerEntry, index) in this.question.possibleAnswers" v-bind:key="answerEntry.text">
          <li class="list-group-item list-group-item-action" :class="{ 'text-danger font-weight-bold': answerEntry.isCorrect }">
            {{index}} - {{ answerEntry.text }} - {{ answerEntry.isCorrect }}
          </li>
        </div>
      </ul>
    </div>
  </div>
  
</template>

<script>
export default {
  name: "QuestionDisplay",
  emits: ["answer-selected"],

  data() {
    return {
      index: 0,
    };
  },

  async created() {
    console.log("Composant QuestionsDisplay 'created'");
  },
  methods: {},
  props: {
    admin:Boolean,
    question: {
      type: Object,
    },
  },
};
</script>

<style>
</style> 