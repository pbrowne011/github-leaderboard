# GitHub Leaderboard

This application displays a leaderboard of GitHub users ranked by their daily
and monthly commit counts.

## Setup

1. Clone the repository
2. Set up the backend:
   - Navigate to the `backend` directory
   - Create a virtual environment: `python -m venv venv`
   - Activate the virtual environment: `source venv/bin/activate` (Unix) or
     `venv\Scripts\activate` (Windows)
   - Install dependencies: `pip install -r requirements.txt`
   - Set the `GITHUB_TOKEN` environment variable with your GitHub personal
     access token
3. Set up the frontend:
   - Navigate to the `frontend` directory
   - Install dependencies: `npm install`
   - Update the `REACT_APP_API_URL` in `.env` with your Heroku app URL
4. Run the application:
   - Start the backend: `python app.py` (from the `backend` directory)
   - Start the frontend: `npm start` (from the `frontend` directory)

## Deployment

1. Deploy the backend to Heroku:
   - Create a new Heroku app
   - Set the `GITHUB_TOKEN` config var in Heroku
   - Push the backend code to Heroku
2. Update the frontend `.env` file with the Heroku app URL
3. Build the frontend: `npm run build`
4. Deploy the frontend to a static hosting service (e.g., Netlify, Vercel, or
   GitHub Pages)
