# Expense Tracker API

A REST API for recording income and expenses per user, built with Django and Django REST Framework on a MySQL database. Each user has a profile that is created automatically on registration, and every transaction belongs to the authenticated user.

## Table of contents

- [Features](#features)
- [Tech stack](#tech-stack)
- [Database schema](#database-schema)
- [API endpoints](#api-endpoints)
- [Getting started](#getting-started)
- [Environment variables](#environment-variables)
- [Project structure](#project-structure)
- [License](#license)

## Features

- User registration and login
- Profile created automatically through a Django signal
- Create, list, update and delete transactions
- Transactions are typed as income or expense
- Users can only access their own profile and transactions
- Filtering by type and date range

## Tech stack

| Layer      | Technology                    |
| ---------- | ----------------------------- |
| Language   | Python 3                      |
| Framework  | Django, Django REST Framework |
| Database   | MySQL                         |
| DB driver  | mysqlclient                   |

## Database schema

![Database schema](database-schema (1).svg)

### auth_user

Django's default `User` model. No changes are made to it.

### Profile

| Field        | Type                      | Notes                         |
| ------------ | ------------------------- | ----------------------------- |
| user         | OneToOneField(User)       | Deleted together with the user |
| full_name    | CharField(150)            |                               |
| email        | EmailField                |                               |
| address      | TextField                 | Optional                      |
| phone_number | CharField(20)             | Optional                      |
| joined_date  | DateField                 | Set when the profile is created |

A `post_save` signal on `User` creates the matching `Profile` whenever a new user is saved.

### Transaction

| Field   | Type                  | Notes                                |
| ------- | --------------------- | ------------------------------------ |
| user    | ForeignKey(User)      | Owner of the transaction             |
| amount  | DecimalField(12, 2)   | Always positive                      |
| date    | DateField             | Date the transaction took place      |
| remarks | CharField(255)        | Short note or description            |
| type    | CharField(10)         | `income` or `expense`                |

### Relationships

- One user has exactly one profile.
- One user has many transactions.

## API endpoints

Base path: `/api/`. All endpoints except register and login require an authenticated user.

| Method | Endpoint                 | Description                    |
| ------ | ------------------------ | ------------------------------ |
| POST   | `/auth/register/`        | Create an account              |
| POST   | `/auth/login/`           | Log in                         |
| GET    | `/profile/`              | View own profile               |
| PUT    | `/profile/`              | Update own profile             |
| GET    | `/transactions/`         | List own transactions          |
| POST   | `/transactions/`         | Create a transaction           |
| GET    | `/transactions/{id}/`    | Retrieve a transaction         |
| PUT    | `/transactions/{id}/`    | Update a transaction           |
| PATCH  | `/transactions/{id}/`    | Partially update a transaction |
| DELETE | `/transactions/{id}/`    | Delete a transaction           |

Query parameters for `GET /transactions/`:

| Parameter   | Example                  | Description          |
| ----------- | ------------------------ | -------------------- |
| `type`      | `?type=expense`          | `income` or `expense` |
| `date_from` | `?date_from=2026-10-01`  | Start date, inclusive |
| `date_to`   | `?date_to=2026-10-31`    | End date, inclusive  |

Example request body for creating a transaction:

```json
{
  "amount": "450.00",
  "date": "2026-10-13",
  "remarks": "Groceries",
  "type": "expense"
}
```

## Getting started

### Prerequisites

- Python 3.10 or newer
- MySQL 8

### Installation

```bash
git clone https://github.com/<your-username>/expense-tracker-api.git
cd expense-tracker-api

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### Database

Create the database in MySQL:

```sql
CREATE DATABASE expense_tracker CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Copy the environment file and fill in your values:

```bash
cp .env.example .env
```

Apply migrations and start the server:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The API is now running at `http://127.0.0.1:8000/api/`.

## Environment variables

| Variable      | Description                  |
| ------------- | ---------------------------- |
| `SECRET_KEY`  | Django secret key            |
| `DEBUG`       | `True` for development       |
| `DB_NAME`     | MySQL database name          |
| `DB_USER`     | MySQL user                   |
| `DB_PASSWORD` | MySQL password               |
| `DB_HOST`     | Database host, e.g. `localhost` |
| `DB_PORT`     | Database port, usually `3306` |

## Project structure

```
expense-tracker-api/
├── config/             # Settings and root URL configuration
├── accounts/           # Profile model, signals, auth endpoints
├── transactions/       # Transaction model, serializers, views
├── docs/               # Database schema diagram
├── manage.py
├── requirements.txt
└── .env.example
```

## License

This project is licensed under the MIT License.