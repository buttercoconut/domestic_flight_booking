export interface FlightStatusResponse {
  flight_number: string;
  status: string;
  departure_time: string;
}

export interface TaxiBookingResponse {
  taxi_id: string;
  driver_name: string;
  eta: string;
}
