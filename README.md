# Stock Alert System

A Django-based web application for monitoring stock prices and sending user alerts when price conditions are met. It supports threshold and duration-based alerts, JWT authentication, and periodic background tasks using Celery.

## Features

- **User Authentication:** Register, login, logout, and JWT-based authentication ([`accounts`](accounts/)).
- **Stock Management:** Predefined stock list, real-time price fetching from Financial Modeling Prep API ([`stocks`](stocks/)).
- **Alerts:**  
  - Threshold and duration-based alerts ([`alerts`](alerts/)).
  - Email notifications when alerts are triggered.
- **Background Tasks:**  
  - Celery + Redis for periodic price fetching and alert checking.
- **REST API:**  
  - Endpoints for user and alert management.
- **Testing:**  # Stock Alert System

A Django-based web application for monitoring stock prices and sending user alerts when price conditions are met. It supports threshold and duration-based alerts, JWT authentication, and periodic background tasks using Celery.

## Features

- **User Authentication:** Register, login, logout, and JWT-based authentication ([`accounts`](accounts/)).
- **Stock Management:** Predefined stock list, real-time price fetching from Financial Modeling Prep API ([`stocks`](stocks/)).
- **Alerts:**  
  - Threshold and duration-based alerts ([`alerts`](alerts/)).
  - Email notifications when alerts are triggered.
- **Background Tasks:**  
  - Celery + Redis for periodic price fetching and alert checking.
- **REST API:**  
  - Endpoints for user and alert management.
- **Testing:**  
  - Unit tests for authentication and alert logic.

## Project Structure

```
accounts/      # User registration, authentication
alerts/        # Alert models, API, permissions, tasks
core/          # Project settings, Celery config, URLs
stocks/        # Stock models, price fetching, seed command
.env           # Environment variables (API keys, DB, email)
manage.py      # Django management script
requirments.txt # Python dependencies
commands.txt   # Celery commands
```

## Setup

1. **Clone the repository**
2. **Install dependencies**
   ```sh
   pip install -r requirments.txt
   ```
3. **Configure environment variables**
   - Edit `.env` with your API keys, email credentials, and database settings.

4. **Apply migrations**
   ```sh
   python manage.py migrate
   ```

5. **Seed stock list**
   ```sh
   python manage.py seed_stocks
   ```

6. **Run the development server**
   ```sh
   python manage.py runserver
   ```

7. **Start Celery worker and beat**
   ```sh
   celery -A core worker --loglevel=info --pool=solo
   celery -A core beat --loglevel=info
   ```

## Redis & Docker

This project uses a Redis server running in a Docker container as the broker for Celery and as the communication medium between the Django server and Celery Background tasks.

To start Redis with Docker:## Redis & Docker

This project uses a Redis server running in a Docker container as the broker for Celery and as the communication medium between the Django server and Celery Background tasks.

To start Redis with Docker:
```sh
docker run -d -p 6379:6379 --name redis
```
Make sure your `.env` and `core/settings.py` point Celery to this Redis instance.

## Stock Price Data Source

This project uses the [Financial Modeling Prep API](https://financialmodelingprep.com/) to fetch real-time stock price data.  
You must set your Financial Modeling Prep API key in the `.env` file for stock price updates to work.

## API Endpoints
// ...existing
```sh
docker run -d -p 6379:6379 --name redis
```
Make sure your `.env` and `core/settings.py` point Celery to this Redis instance.

## API Endpoints

- **Accounts:**  
  - `POST /api/accounts/register/` — Register new user  
  - `POST /api/accounts/login/` — Obtain JWT tokens  
  - `POST /api/accounts/logout/` — Logout (blacklist token)  
  - `POST /api/accounts/refresh/` — Refresh JWT token

- **Alerts:**  
  - `GET /api/alerts/` — List user alerts  
  - `GET /api/alerts/{id}/` — Get an alert 
  - `POST /api/alerts/` — Create alert  
  - `PUT /api/alerts/{id}/` — Update alert  
  - `PATCH /api/alerts/{id}/` — Update field in alert  
  - `DELETE /api/alerts/{id}/` — Delete alert  
  - `DELETE /api/alerts/delete_all/` — Delete all user alerts

## Testing

Run unit tests with:
```sh
python manage.py test
```

## Background Tasks

- **Fetch stock prices:** Every minute ([`stocks/tasks.py`](stocks/tasks.py))
- **Check alerts:** Every minute ([`alerts/tasks.py`](alerts/tasks.py))

## Configuration

- **Database:** PostgreSQL (set credentials in `.env`)
- **Email:** SMTP (Gmail recommended; set credentials in `.env`)
- **Celery:** Redis as broker and backend (via Docker)

## License

MIT License

---

**For more details, see the source files:**
- [core/settings.py](core/settings.py)
-
  - Unit tests for authentication and alert logic.

## Project Structure

```
accounts/      # User registration, authentication
alerts/        # Alert models, API, permissions, tasks
core/          # Project settings, Celery config, URLs
stocks/        # Stock models, price fetching, seed command
.env           # Environment variables (API keys, DB, email)
manage.py      # Django management script
requirments.txt # Python dependencies
commands.txt   # Celery commands
```

## Setup

1. **Clone the repository**
2. **Install dependencies**
   ```sh
   pip install -r requirments.txt
   ```
3. **Configure environment variables**
   - Edit `.env` with your API keys, email credentials, and database settings.

4. **Apply migrations**
   ```sh
   python manage.py migrate
   ```

5. **Seed stock list**
   ```sh
   python manage.py seed_stocks
   ```

6. **Run the development server**
   ```sh
   python manage.py runserver
   ```

7. **Start Celery worker and beat**
   ```sh
   celery -A core worker --loglevel=info --pool=solo
   celery -A core beat --loglevel=info
   ```

## API Endpoints

- **Accounts:**  
  - `POST /api/accounts/register/` — Register new user  
  - `POST /api/accounts/login/` — Obtain JWT tokens  
  - `POST /api/accounts/logout/` — Logout (blacklist token)  
  - `POST /api/accounts/refresh/` — Refresh JWT token

- **Alerts:**  
  - `GET /api/alerts/` — List user alerts  
  - `GET /api/alerts/{id}/` — Get an alert 
  - `POST /api/alerts/` — Create alert  
  - `PUT /api/alerts/{id}/` — Update alert  
  - `PATCH /api/alerts/{id}/` — Update field in alert  
  - `DELETE /api/alerts/{id}/` — Delete alert  
  - `DELETE /api/alerts/delete_all/` — Delete all user alerts

## Testing

Run unit tests with:
```sh
python manage.py test
```

## Background Tasks

- **Fetch stock prices:** Every minute ([`stocks/tasks.py`](stocks/tasks.py))
- **Check alerts:** Every minute ([`alerts/tasks.py`](alerts/tasks.py))

## Configuration

- **Database:** PostgreSQL (set credentials in `.env`)
- **Email:** SMTP (Gmail recommended; set credentials in `.env`)
- **Celery:** Redis as broker and backend

## License

MIT License

---

**For more details, see the source files:**
- [core/settings.py](core/settings.py)
- [accounts/views.py](accounts/views.py)
- [alerts/models.py](alerts/models.py)
-