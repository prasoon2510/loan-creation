
# Loan Creation API

A Python-based Loan Creation API project built using
FastAPI, Requests and uv.

## Project Overview

This project integrates with the Loan Management Gateway
to create loans and retrieve loan details using REST APIs.

## Technologies Used

- Python
- FastAPI
- Requests
- python-dotenv
- uv
- Uvicorn
- Git and GitHub

## Project Structure

```text
loan-creation-api/
│
├── services/
│   ├── loan_creation_service.py
│   └── loan_details_service.py
│
├── main.py
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd loan-creation-api
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file in the project root.

Configure the required API URLs, credentials
and other environment variables.

Never commit your actual credentials to GitHub.

### 4. Run the application

```bash
uv run python main.py
```

If running the FastAPI application through Uvicorn:

```bash
uv run uvicorn main:app --reload
```

## Features

- Create loans using POST API.
- Retrieve loan details using GET API.
- Handle API responses.
- Handle HTTP exceptions.
- Manage configuration through environment variables.
- Integrate with external Loan Management Gateway APIs.

## Dependency Management

Add a dependency:

```bash
uv add requests
```

Remove a dependency:

```bash
uv remove requests
```

Synchronize dependencies:

```bash
uv sync
```

## Git Workflow

1. Create a feature branch.
2. Develop and test your changes.
3. Commit your changes.
4. Push your feature branch.
5. Create a Pull Request.
6. Resolve merge conflicts before merging into main.

## Security

- Do not commit `.env` files.
- Do not expose API usernames or passwords.
- Keep credentials in environment variables.
- Never commit sensitive loan information.

## Contributors

Loan Creation API Development Team.
