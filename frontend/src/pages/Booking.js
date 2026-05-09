import React, { useState } from 'react';
import axios from 'axios';

function Booking() {
  const [form, setForm] = useState({
    user_id: 1,
    flight_id: 1,
    seat_number: "12A",
    passenger_name: "John Doe",
    passenger_id: "A1234567",
  });
  const [response, setResponse] = useState(null);

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const res = await axios.post(
        'http://localhost:8000/bookings/reserve',
        form
      );
      setResponse(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Book a Flight</h2>
      ?{response && (
        <pre>{JSON.stringify(response, null, 2)}</pre>
      )}?
      ?{!response && (
        <form onSubmit={handleSubmit}>
          <label>
            User ID:
            <input
              type="number"
              name="user_id"
              value={form.user_id}
              onChange={handleChange}
            />
          </label>
          <br />
          <label>
            Flight ID:
            <input
              type="number"
              name="flight_id"
              value={form.flight_id}
              onChange={handleChange}
            />
          </label>
          <br />
          <label>
            Seat Number:
            <input
              type="text"
              name="seat_number"
              value={form.seat_number}
              onChange={handleChange}
            />
          </label>
          <br />
          <label>
            Passenger Name:
            <input
              type="text"
              name="passenger_name"
              value={form.passenger_name}
              onChange={handleChange}
            />
          </label>
          <br />
          <label>
            Passenger ID:
            <input
              type="text"
              name="passenger_id"
              value={form.passenger_id}
              onChange={handleChange}
            />
          </label>
          <br />
          <button type="submit">Reserve</button>
        </form>
      )}?
    </div>
  );
}

export default Booking;
