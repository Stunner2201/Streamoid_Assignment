#  Streamoid  Backend

A FastAPI-based backend for managing products, uploading CSVs, and providing search/list functionality.  
The project is containerized using Docker for easy setup and deployment.

---

##  Project Structure
~~~
├── app
│   ├── main.py               # FastAPI app entry point
│   ├── database.py           # SQLite + SQLModel configuration
│   ├── models.py             # Product model
│   ├── routes
│   │   ├── products.py       # Product listing & search endpoints
│   │   └── upload.py         # CSV file upload endpoint
│   └── utils
│       └── validators.py     # Row validation logic
├── data                      # Persistent database storage
├── uploads                   # Uploaded CSV files
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env
└── README.md
~~~
##  Project Description

This FastAPI project allows you to:

- Upload product CSV files.
- List all products with pagination.
- Search products with filters like brand, color, and price range.

The project uses **SQLite** for persistent storage and **SQLModel** as the ORM. Dockerized setup ensures easy deployment.

---

##  Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Stunner2201/Streamoid_Assignment
cd Streamoid_Assignment
```
### 2. Create .env file
```bash
DATABASE_URL=sqlite:///./data/test.db
```

### 3. Build and run the Docker container
#### Option A:Windows / Mac with Docker Desktop
```bash
docker-compose build
docker-compose up
```
#### Option B:Mac without Docker Desktop (using Colima)
```bash
brew install colima docker
colima start
docker-compose build
docker-compose up
```
### 4. Access the application
```bash
http://127.0.0.1:8000/docs
```
### 5. Testing the Application
#### 1. You’ll see all available endpoints:
```bash
- /upload-csv/ → Upload product CSV file
- /products/ → List all products
- /products/search/ → Search products
```

#### 2. Click on the “Try it out” button for any endpoint you want to test.
```bash
- For Upload CSV, click Try it out → Choose File → Execute.
- For List Products or Search Products, click Try it out → Enter parameters → Execute.
- You’ll see the response (JSON) and status code directly below the request box.
```



