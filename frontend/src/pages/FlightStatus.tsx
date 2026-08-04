import React, { useState } from 'react';
import FlightStatusForm from '../components/FlightStatusForm';
import { FlightStatusResponse } from '../types/index';
import { getFlightStatus } from '../services/api';

const FlightStatus: React.FC = () => {
  const [flightNumber, setFlightNumber] = useState('');
  const [result, setResult] = useState<FlightStatusResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    try {
      const data = await getFlightStatus(flightNumber);
      setResult(data);
    } catch (err) {
      setError('Failed to fetch flight status.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-md mx-auto bg-white p-6 rounded shadow">
      <h2 className="text-2xl font-semibold mb-4">Check Flight Status</h2>
      <FlightStatusForm
        flightNumber={flightNumber}
        setFlightNumber={setFlightNumber}
        onSubmit={handleSubmit}
        loading={loading}
      />
      {loading && <p className="mt-4 text-gray-500">Loading...</p>}
      {error && <p className="mt-4 text-red-600">{error}</p>}
      {result && (
        <div className="mt-6 p-4 bg-gray-50 rounded">
          <p className="font-medium">Flight: {result.flight_number}</p>
          <p>Status: {result.status}</p>
          <p>Departure Time: {result.departure_time}</p>
        </div>
      )}
    </div>
  );
};

export default FlightStatus;
