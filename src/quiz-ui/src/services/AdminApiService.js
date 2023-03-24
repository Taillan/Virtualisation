import axios from "axios";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },

  postLogin(password) {
    console.debug("postLogin");
    let response = this.call("POST", "login", { "password": password });
    return response;
  },

  getAllQuestion() {
    console.debug("getAllQuestion");
    let response = this.call("GET", "questions");
    return response;
  },

  deleteQuestion(position,token) {
    console.debug("deleteQuestion");
    this.call("DELETE", "questions/"+position,null,token);
  },

  editQuestion(oldposition,text, title, image, position, texteA, answerA, texteB, answerB, texteC, answerC, texteD, answerD,token) {
    console.debug("editQuestion");
    let payload = {
      "text": text,
      "title": title,
      "image": image,
      "position": position,
      "possibleAnswers":
        [
          { "text": texteA, "isCorrect": answerA },
          { "text": texteB, "isCorrect": answerB },
          { "text": texteC, "isCorrect": answerC },
          { "text": texteD, "isCorrect": answerD },
        ]
    }
    this.call("PUT", "questions/"+oldposition,payload,token);
  },

  postAddQuestion(text, title, image, position, texteA, answerA, texteB, answerB, texteC, answerC, texteD, answerD,token) {
    console.debug("postAddQuestion");
    let payload = {
      "text": text,
      "title": title,
      "image": image,
      "position": position,
      "possibleAnswers":
        [
          { "text": texteA, "isCorrect": answerA },
          { "text": texteB, "isCorrect": answerB },
          { "text": texteC, "isCorrect": answerC },
          { "text": texteD, "isCorrect": answerD },
        ]
    }
    this.call("POST", "questions", payload,token);
    return;
  }
}