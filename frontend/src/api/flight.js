import axios from 'axios';

const API_BASE = process.env.VUE_APP_API_BASE || 'http://localhost:8000/api';

export const searchFlights = (params) => {
  return axios.get(`${API_BASE}/flights/search`, { params });
};

export const reserveFlight = (bookingData) => {
  return axios.post(`${API_BASE}/bookings`, bookingData);
};
