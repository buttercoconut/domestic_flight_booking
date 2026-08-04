import React, { useState } from 'react';
import TaxiBookingForm from '../components/TaxiBookingForm';
import { TaxiBookingResponse } from '../types/index';
import { bookTaxi } from '../services/api';

const BookTaxi: React.FC = () => {
  const [pickup, setPickup] = useState('');
  const [destination, setDestination] = useState('');
  const [result, setResult] = useState<TaxiBookingResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    try {
      const data = await bookTaxi(pickup, destination);
      setResult(data);
    } catch (err) {
      setError('Failed to book taxi.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-md mx-auto bg-white p-6 rounded shadow">
      <h2 className="text-2xl font-semibold mb-4">Book a Taxi</h2>
      <TaxiBookingForm
        pickup={pickup}
        setPickup={setPickup}
        destination={destination}
        setDestination={setDestination}
        onSubmit={handleSubmit}
        loading={loading}
      />
      {loading && <p className="mt-4 text-gray-500">Loading...</p>}
      {error && <p className="mt-4 text-red-600">{error}</p>}
      {result && (
        <div className="mt-6 p-4 bg-gray-50 rounded">
          <p className="font-medium">Taxi ID: {result.taxi_id}</p>
          <p>Driver: {result.driver_name}</p>
          <p>Estimated Arrival: {result.eta}</p>
        </div>
      )}
    </div>
  );
};

export default BookTaxi;
