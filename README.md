# Booking System

A web application built using Django and Django REST Framework (DRF) that allows users to manage their booking. This system supports JWT authentication for secure access and utilizes drf-spectacular for comprehensive API documentation.

## Features

- **User Authentication**
  - Signup
  - Login (JWT)
  - Token Refresh
  - Logout

- **Booking Management**
  - Create Booking
  - List User Booking
  - Update Booking Status

- **API Documentation**
  - Swagger UI with organized tags for better navigation

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.10 or higher
- Django 5.0.6
- Django REST Framework 3.15.1

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/booking_system.git
    cd booking_system
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv bookingvenv
    source bookingvenv/bin/activate  # On Windows use `bookingvenv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Run the server:**

    ```bash
    python manage.py runserver
    ```

## Usage

### API Documentation

Navigate to `http://127.0.0.1:8000/schema/swagger-ui/` to view the Swagger UI documentation.

### Endpoints

- **Authentication:**
  - `POST /api/auth/signup/`: User signup
  - `POST /api/auth/login/`: User login to obtain JWT token
  - `POST /api/auth/login/refresh/`: Refresh JWT token
  - `POST /api/auth/logout/`: User logout

- **Booking:**
  - `POST /api/booking/create/`: Create a new booking
  - `GET /api/booking/`: List booking for the authenticated user
  - `PUT /api/booking/<id>/update/`: Update the status of a booking