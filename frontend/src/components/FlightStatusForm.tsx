import React from 'react';

interface Props {
  flightNumber: string;
  setFlightNumber: (value: string) => void;
  onSubmit: (e: React.FormEvent) => void;
  loading: boolean;
}

const FlightStatusForm: React.FC<Props> = ({
  flightNumber,
  setFlightNumber,
  onSubmit,
  loading,
}) => {
  return (
    <form onSubmit={onSubmit} className="space-y-4">
      <div>
        <label className="block text-sm font-medium text-gray-700">
          Flight Number
        </label>
        <input
          type="text"
          value={flightNumber}
          onChange={(e) => setFlightNumber(e.target.value)}
          className="mt-1 block w-full rounded border-gray-300 shadow-sm"
          placeholder="e.g., 1234"
          required
        />
      </div>
      <button
        type="submit"
        disabled={loading}
        className="w-full inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700"
      >
        {loading ? 'Checking...' : 'Check Status'}
      </button>
    </form>
  );
};

export default FlightStatusForm;
