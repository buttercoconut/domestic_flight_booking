import axios from 'axios';
import { FlightStatusResponse, TaxiBookingResponse } from '../types/index';

const API_BASE = process.env.REACT_APP_API_BASE || 'http://localhost:8000/api';

export const getFlightStatus = async (flightNumber: string): Promise<FlightStatusResponse> => {
  const response = await axios.get<FlightStatusResponse>(`${API_BASE}/flight-status/${flightNumber}`);
  return response.data;
};

export const bookTaxi = async (
  pickup: string,
  destination: string
): Promise<TaxiBookingResponse> => {
  const response = await axios.post<TaxiBookingResponse>(`${API_BASE}/taxi-booking`, {
    pickup,
    destination,
  });
  return response.data;
};
