<template>
  <div class="app-container">
    <h1>Word Count</h1>
    <div><img src="https://voxy.com/wp-content/uploads/2024/05/voxy_logo_horizontal_aqua_purple-1-300x67.webp" alt="Voxy Logo" width="300" height="67"></div>
    <form @submit.prevent="submitSentence" class="form">
      <label for="sentence">Enter a sentence:</label>
      <textarea
        type="text"
        id="sentence"
        v-model="sentence"
        placeholder="Type a sentence here"
        class="input"
      />
      <button type="submit" class="submit-button">Submit</button>
    </form>
    <div v-if="wordCount !== null" class="word-count">
      <p>Word count: {{ wordCount }}</p>
    </div>
    <div v-if="errorMessage" class="error-message">
      <p>{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const sentence = ref('');
const wordCount = ref(null);
const errorMessage = ref(null);

const submitSentence = async () => {
  errorMessage.value = null;
  wordCount.value = null;
  try {
    if (sentence.value.trim() === "") {
      throw new Error('Sentence cannot be empty');
    }
    const response = await fetch(`http://${import.meta.env.VITE_FLASK_HOST}:${import.meta.env.VITE_FLASK_PORT}/count_words`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify([sentence.value]), // Send as array
    });
    if (!response.ok) throw new Error('Failed to fetch word count');
    const data = await response.json();
    wordCount.value = data[0];
  } catch (error) {
    errorMessage.value = 'Error: ' + error.message;
  }
};
</script>

<style scoped>
.app-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.form {
  margin-top: 20px;
}

.input {
  padding: 10px;
  width: 100%;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  height: 60px;
}

.submit-button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #0056b3;
}

.word-count {
  margin-top: 20px;
}

.error-message {
  margin-top: 20px;
  color: red;
}
</style>
