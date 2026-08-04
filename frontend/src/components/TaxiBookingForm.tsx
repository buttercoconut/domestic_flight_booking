import React from 'react';

interface Props {
  pickup: string;
  setPickup: (value: string) => void;
  destination: string;
  setDestination: (value: string) => void;
  onSubmit: (e: React.FormEvent) => void;
  loading: boolean;
}

const TaxiBookingForm: React.FC<Props> = ({
  pickup,
  setPickup,
  destination,
  setDestination,
  onSubmit,
  loading,
}) => {
  return (
    <form onSubmit={onSubmit} className="space-y-4">
      <div>
        <label className="block text-sm font-medium text-gray-700">
          Pickup Location
        </label>
        <input
          type="text"
          value={pickup}
          onChange={(e) => setPickup(e.target.value)}
          className="mt-1 block w-full rounded border-gray-300 shadow-sm"
          placeholder="e.g., Terminal 1"
          required
        />
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700">
          Destination
        </label>
        <input
          type="text"
          value={destination}
          onChange={(e) => setDestination(e.target.value)}
          className="mt-1 block w-full rounded border-gray-300 shadow-sm"
          placeholder="e.g., Hotel XYZ"
          required
        />
      </div>
      <button
        type="submit"
        disabled={loading}
        className="w-full inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700"
      >
        {loading ? 'Booking...' : 'Book Taxi'}
      </button>
    </form>
  );
};

export default TaxiBookingForm;
