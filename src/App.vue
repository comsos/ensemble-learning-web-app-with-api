<script setup>
import HelloWorld from "./components/HelloWorld.vue";

import { ref } from "vue";

const result = ref(0);
const arr = ref([]);

const clicked = ref(false);

const age = ref("");

function request() {
  clicked.value = true;
  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
    body: JSON.stringify({
      array: arr.value,
    }),
  };
  fetch("http://127.0.0.1:5000/predict", requestOptions)
    .then((response) => response.json())
    .then((data) => (result.value = data.result));
}
function appendToArray(item, index) {
  console.log(item);
  arr.value[index] = item;
}
function clearButton() {
  age.value = "";
  clicked.value = false;
}
</script>

<template>
  <div>
    <div class="h-screen flex flex-col items-center justify-center">
      <h1 class="text-xl font-bold" :class="{ invisible: !clicked }">
        {{ result == 0 ? "Least likely" : "Most Likely" }}
      </h1>
      <h1 class="text-lg">{{ arr }}</h1>

      <div class="flex flex-row space-x-12 py-12">
        <div class="flex flex-col space-y-6">
          <input
            type="number"
            class="border-solid border-black border-2"
            placeholder="Age"
            v-model="age"
            @blur="appendToArray(age, 0)"
          />
          Age

          <input
            type="number"
            class="border-solid border-black border-2"
            placeholder="Sex"
            v-model="sex"
            @blur="appendToArray(sex, 1)"
          />
          Sex (1 = Male, 0 = Female)

          <input
            type="number"
            class="border-solid border-black border-2"
            placeholder="Chest Pain Type"
            v-model="cpt"
            @blur="appendToArray(cpt, 2)"
          />
          Chest Pain Type (1-4)

          <input
            type="number"
            class="border-solid border-black border-2"
            placeholder="Resting Blood Pressure"
            v-model="rbp"
            @blur="appendToArray(rbp, 3)"
          />
          Resting Blood Pressure

          <input
            type="number"
            class="border-solid border-black border-2"
            placeholder="Cholesterol in mg/dl fetched via BMI sensor"
            v-model="cbmi"
            @blur="appendToArray(cbmi, 4)"
          />
          Cholesterol in mg/dl fetched via BMI Sensor

          <input
            type="number"
            class="border-solid border-black border-2"
            placeholder="Fasting Blood Sugar"
            v-model="fbs"
            @blur="appendToArray(fbs, 5)"
          />
          Fasting Blood Sugar (1 = >120 0 = &lt120)
        </div>
        <div class="flex flex-col space-y-6">
          <input
            type="number"
            class="border-solid border-black border-2"
            placeholder="Resting ElectroCardiographic Results"
            v-model="rer"
            @blur="appendToArray(rer, 6)"
          />
          Resting ECG

          <input
            type="number"
            class="border-solid border-black border-2"
            placeholder="Maximum Heart Rate Achieved"
            v-model="mhra"
            @blur="appendToArray(mhra, 7)"
          />
          Maximum Heart Rate Achieved

          <input
            type="number"
            class="border-solid border-black border-2"
            placeholder="Exercise Induced Angine"
            v-model="eia"
            @blur="appendToArray(eia, 8)"
          />
          Exercise Induced Agnina (1 = Yes, 0 = No)
          <input
            type="number"
            class="border-solid border-black border-2"
            placeholder="Previous Peak"
            v-model="pp"
            @blur="appendToArray(pp, 9)"
          />
          Previous Peak
          <input
            type="number"
            class="border-solid border-black border-2"
            placeholder="Slope"
            v-model="s"
            @blur="appendToArray(s, 10)"
          />
          Slope
          <input
            type="number"
            class="border-solid border-black border-2"
            placeholder="Number of Major Vessels"
            v-model="nmv"
            @blur="appendToArray(nmv, 11)"
          />
          Number of Major Vessels
        </div>
      </div>
      Thal Rate
      <input
        type="number"
        class="border-solid border-black border-2 mb-4"
        placeholder="Thal Rate"
        v-model="tr"
        @blur="appendToArray(tr, 12)"
      />
      <div class="flex flex-row space-x-4">
        <button
          @click="request"
          type="button"
          class="bg-black h-12 w-24 text-white"
        >
          Predict
        </button>
        <button
          @click="clearButton"
          type="button"
          class="bg-black h-12 w-24 text-white"
        >
          Clear
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
.fields {
  flex: auto;
  flex-direction: row;
}
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
