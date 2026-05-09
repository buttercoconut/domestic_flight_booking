<template>
  <div class="flight-list">
    <h2>Flight Search Results</h2>
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <ul v-else>
      <li v-for="flight in flights" :key="flight.id" class="flight-item">
        <div>
          <strong>{{ flight.flight_number }}</strong> - {{ flight.departure_airport }} → {{ flight.arrival_airport }}
        </div>
        <div>
          Departure: {{ formatDate(flight.departure_time) }} | Price: {{ flight.price }}원
        </div>
        <button @click="selectFlight(flight)">Select</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { searchFlights } from '../api/flight';

const props = defineProps({
  query: { type: Object, required: true },
});

const flights = ref([]);
const loading = ref(false);
const error = ref('');

const fetchFlights = async () => {
  loading.value = true;
  error.value = '';
  try {
    const { data } = await searchFlights(props.query);
    flights.value = data.results;
  } catch (e) {
    error.value = '검색에 실패했습니다. 다시 시도해주세요.';
  } finally {
    loading.value = false;
  }
};

const formatDate = (iso) => new Date(iso).toLocaleString();

const emit = defineEmits(['flightSelected']);
const selectFlight = (flight) => emit('flightSelected', flight);

onMounted(fetchFlights);
</script>

<style scoped>
.flight-list { padding: 1rem; }
.flight-item { margin-bottom: 1rem; }
.loading, .error { color: #888; }
</style>
