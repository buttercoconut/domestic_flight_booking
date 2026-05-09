import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div>
      <h1>Domestic Flight Booking</h1>
      <nav>
        <ul>
          <li>
            <Link to="/booking">Book a Flight</Link>
          </li>
          <li>
            <Link to="/payment">Make a Payment</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}

export default Home;
