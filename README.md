# Blog Application

This blog application, built using **FastAPI**, provides a fast and scalable platform for users to create, read, update, and delete blog posts. It combines cutting-edge technologies to deliver a high-performance and reliable solution for managing blog content.

## Key Features and Technologies

### 1. **FastAPI Backend**
- The application leverages FastAPI for its high-performance backend.
- Ensures rapid response times and a robust API for managing blog content.

### 2. **PostgreSQL Database**
- Uses PostgreSQL as the relational database.
- Provides secure, efficient, and scalable data storage for blog posts and user data.

### 3. **Pydantic for Data Validation**
- Utilized for data validation and serialization.
- Ensures that input data is validated before interacting with the database.

### 4. **SQLAlchemy ORM**
- Implements SQLAlchemy as the Object-Relational Mapping (ORM) tool.
- Enables seamless interaction between Python objects and the PostgreSQL database.

## Project Highlights
This project combines:
- **FastAPI's speed** for quick and efficient API responses.
- **PostgreSQL's reliability** for robust data storage.
- **Pydantic's validation** for ensuring data integrity.
- **SQLAlchemy's ORM capabilities** for smooth database operations.

## Getting Started
Follow these steps to set up and run the application locally:

### Prerequisites
- Python 3.9+
- PostgreSQL 12+
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/blog-application.git
   cd blog-application
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
    ```bash
   pip install -r requirements.txt
   ```
4. Run sever:
    ```bash
   fastapi dev app/main.py
   ```
