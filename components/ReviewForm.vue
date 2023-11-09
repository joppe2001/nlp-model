<template>
    <div class="review-form">
      <h1>Restaurant Review Sentiment Analysis</h1>
      <textarea v-model="review" placeholder="Write your review here..."></textarea>
      <button @click="submitReview">Analyze Sentiment</button>
      <p v-if="prediction">Prediction: {{ prediction }}</p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ReviewForm',
    setup() {
      const review = ref('');
      const prediction = ref('');
  
      async function submitReview() {
        try {
          const response = await fetch('http://127.0.0.1:5000/api/predict', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ review: review.value }),
          });
          const data = await response.json();
          prediction.value = data.prediction;
        } catch (error) {
          console.error('Error:', error);
        }
      }
  
      return { review, prediction, submitReview };
    },
  };
  </script>
  
  <style scoped>
  .review-form {
    max-width: 500px;
    margin: 50px auto;
    padding: 20px;
    text-align: center;
  }
  
  textarea {
    width: 100%;
    height: 150px;
    margin-bottom: 20px;
    padding: 10px;
    font-size: 16px;
  }
  
  button {
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
  }
  </style>
  