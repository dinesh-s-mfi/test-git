from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="HR Use Case API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to HR Use Case API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/employees")
def get_employees():
    """Get list of employees"""
    return {
        "employees": [
            {"id": 1, "name": "John Doe", "department": "Engineering"},
            {"id": 2, "name": "Jane Smith", "department": "HR"},
        ]
    }

@app.post("/api/employees")
def create_employee(employee: dict):
    """Create a new employee"""
    return {"message": "Employee created successfully", "employee": employee}


def main():
    """Main function to run the server locally"""
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
