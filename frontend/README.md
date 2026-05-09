# Domestic Flight Booking Frontend

## Project Structure
```
frontend/
├─ public/
│  └─ index.html
├─ src/
│  ├─ api/
│  │  └─ flight.js
│  ├─ components/
│  │  └─ FlightList.vue
│  ├─ views/
│  │  └─ SearchPage.vue
│  ├─ router/
│  │  └─ index.js
│  ├─ store/
│  │  └─ index.js
│  ├─ App.vue
│  └─ main.js
└─ package.json
```

## How to Run
1. Install dependencies:
   ```bash
   npm install
   ```
2. Start dev server:
   ```bash
   npm run dev
   ```
3. Open `http://localhost:5173` in your browser.

## Notes
- API base URL is set via `VUE_APP_API_BASE` env variable.
- Flight search results are displayed in `FlightList.vue`.
- The search form is in `SearchPage.vue`.
- Vuex store is currently a placeholder for future state management.
