<template>
  <div class="search-page">
    <h1>Domestic Flight Search</h1>
    <form @submit.prevent="onSearch">
      <label>From:<input v-model="search.from" required /</label>
      <label>To:<input v-model="search.to" required /</label>
      <label>Date:<input type="date" v-model="search.date" required /</label>
      <button type="submit">Search</button>
    </form>
    <FlightList v-if="showResults" :query="searchParams" @flightSelected="onFlightSelected" />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import FlightList from '../components/FlightList.vue';

const search = ref({ from: '', to: '', date: '' });
const showResults = ref(false);
const searchParams = ref({});

const onSearch = () => {
  searchParams.value = {
    departure_airport: search.value.from,
    arrival_airport: search.value.to,
    date: search.value.date,
  };
  showResults.value = true;
};

const onFlightSelected = (flight) => {
  console.log('Selected flight', flight);
  // 예약 로직 호출 예정
};
</script>

<style scoped>
.search-page { padding: 1rem; }
label { display: block; margin-bottom: 0.5rem; }
</style>
