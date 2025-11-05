# HR Use Case 1

A human resources management application with a Node.js frontend and FastAPI Python backend.

## Project Structure

```
HR-usecase1/
├── frontend/          # Node.js frontend application
├── backend/           # FastAPI Python backend application
└── README.md          # This file
```

## Technology Stack

### Frontend
- Node.js
- (Add specific frameworks/libraries: React, Vue, Express, etc.)

### Backend
- Python 3.8+
- FastAPI
- (Add database: PostgreSQL, MySQL, SQLite, etc.)

## Prerequisites

- Node.js (v14 or higher recommended)
- npm or yarn
- Python 3.8+
- pip

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run the backend server:
```bash
uvicorn main:app --reload
```

The backend will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
# or
yarn install
```

3. Run the development server:
```bash
npm start
# or
yarn start
```

The frontend will be available at `http://localhost:3000` (or the configured port)

## API Documentation

Once the backend is running, you can access:
- API Documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API Documentation (ReDoc): `http://localhost:8000/redoc`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

(Mention your license here)

