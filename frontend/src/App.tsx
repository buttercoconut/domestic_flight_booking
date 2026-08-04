import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import FlightStatus from './pages/FlightStatus';
import BookTaxi from './pages/BookTaxi';

const App: React.FC = () => {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <nav className="bg-white shadow">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex items-center justify-between h-16">
              <div className="flex items-center">
                <Link to="/" className="text-xl font-bold text-indigo-600">
                  Domestic Flight Booking
                </Link>
              </div>
              <div className="flex space-x-4">
                <Link
                  to="/"
                  className="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium"
                >
                  Home
                </Link>
                <Link
                  to="/flight-status"
                  className="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium"
                >
                  Flight Status
                </Link>
                <Link
                  to="/book-taxi"
                  className="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium"
                >
                  Book Taxi
                </Link>
              </div>
            </div>
          </div>
        </nav>
        <main className="p-6">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/flight-status" element={<FlightStatus />} />
            <Route path="/book-taxi" element={<BookTaxi />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
};

export default App;
