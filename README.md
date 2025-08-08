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

## License## Deployment on AWS

## Deployment on AWS (with Docker Compose)

### How I Deployed This Server on AWS EC2

1. **Provisioned an EC2 Instance**
   - I launched an Ubuntu EC2 instance on AWS and configured security groups to allow HTTP (port 80), HTTPS (port 443), and SSH (port 22).

2. **Installed System Packages**
   - I updated the system and installed Docker and Docker Compose:
     ```sh
     sudo apt update && sudo apt upgrade -y
     sudo apt install docker.io docker-compose -y
     ```

3. **Cloned the Project**
   - I cloned this repository to the EC2 instance:
     ```sh
     git clone https://github.com/mazenosama493/stock_alert_system.git
     cd stock_alert_system
     ```

4. **Configured Environment Variables**
   - I created a `.env` file with my API keys, database credentials, and email settings.

5. **Configured Docker Compose**
   - I used the provided `docker-compose.yml` to orchestrate the Django app, PostgreSQL, and Redis containers.
   - The Docker Compose file builds the Django app image, runs migrations, seeds stocks, and starts Gunicorn, Celery worker, and Celery beat.

6. **Started the Application Stack**
   - I started all services using Docker Compose:
     ```sh
     sudo docker-compose up --build -d
     ```
   - This command builds the Docker image for the Django app and starts all containers (web, db, redis, celery, celerybeat).

7. **Verified Everything Was Running**
   - I checked the logs and container status:
     ```sh
     sudo docker-compose ps
     sudo docker-compose logs web
     ```

---

Now, the server runs on AWS EC2 using Docker Compose.  
All components (Django, PostgreSQL, Redis, Celery worker, Celery beat) are managed as containers.  
Celery tasks and background jobs are automatically started with the stack.

**Tip:**  
You can restart all services with:
```sh
sudo docker-compose restart
```
And view logs with:
```sh
sudo docker-