import React, { useState } from 'react';
import axios from 'axios';

function Payment() {
  const [form, setForm] = useState({
    booking_id: 1,
    amount: 150.0,
    payment_method: "credit_card",
  });
  const [response, setResponse] = useState(null);

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const res = await axios.post(
        'http://localhost:8000/payments/process',
        form
      );
      setResponse(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Make a Payment</h2>
      ?{response && (
        <pre>{JSON.stringify(response, null, 2)}</pre>
      )}?
      ?{!response && (
        <form onSubmit={handleSubmit}>
          <label>
            Booking ID:
            <input
              type="number"
              name="booking_id"
              value={form.booking_id}
              onChange={handleChange}
            />
          </label>
          <br />
          <label>
            Amount:
            <input
              type="number"
              step="0.01"
              name="amount"
              value={form.amount}
              onChange={handleChange}
            />
          </label>
          <br />
          <label>
            Payment Method:
            <input
              type="text"
              name="payment_method"
              value={form.payment_method}
              onChange={handleChange}
            />
          </label>
          <br />
          <button type="submit">Pay</button>
        </form>
      )}?
    </div>
  );
}

export default Payment;
