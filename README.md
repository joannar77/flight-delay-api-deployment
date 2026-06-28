![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-009688)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Model%20Serving-orange)
![Pytest](https://img.shields.io/badge/Pytest-Automated%20Testing-green)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

# ✈️ Flight Delay Prediction API with FastAPI & Docker

A production-style REST API developed to deploy a trained machine learning model for flight delay prediction. The application exposes prediction endpoints through FastAPI, incorporates automated testing with pytest, and supports containerized deployment using Docker.

---

# Project Overview

This project demonstrates the deployment phase of the machine learning lifecycle by transforming a trained predictive model into an accessible web service.

The API accepts flight-related inputs, processes requests using a trained regression model, and returns predicted departure delays through HTTP endpoints.

---

# 🎥 API Demonstration

A short demonstration of the deployed REST API is available on Vimeo. The video shows the FastAPI application running inside a Docker container, submitting HTTP requests to the prediction endpoint, and returning real-time machine learning predictions through the deployed service.

▶️ **Watch the API Demonstration**

https://vimeo.com/1205144651

---

# Technologies

## Backend Development

- Python
- FastAPI
- Uvicorn

## Machine Learning

- Scikit-learn
- NumPy
- Pandas

## Testing

- Pytest

## Deployment

- Docker

## Version Control

- Git
- GitHub

---

# Features

- REST API endpoint for flight delay prediction
- JSON-based request and response handling
- Automated unit testing
- Docker containerization
- Machine learning model deployment
- Airport code encoding support
- HTTP endpoint validation

---

# Project Architecture

```text
.
├── main.py
├── test_main.py
├── Dockerfile
├── requirements.txt
├── finalized_model.pkl
├── airport_encodings.json
├── README.md
└── flight_delay_api.ipynb
```

---

# API Endpoints

## Root Endpoint

```http
GET /
```

Returns a status message confirming API availability.

Example Response:

```json
{
  "message": "API is operational"
}
```

---

## Delay Prediction Endpoint

```http
GET /predict/delays
```

### Parameters

| Parameter | Type | Description |
|------------|------|-------------|
| arrival_airport | string | Airport code (e.g., LAX) |
| dep_time | integer | Departure time (HHMM) |
| arr_time | integer | Arrival time (HHMM) |

Example Request:

```http
/predict/delays?arrival_airport=LAX&dep_time=1400&arr_time=1630
```

Example Response:

```json
{
  "predicted_departure_delay_minutes": 3.09
}
```

---

# Automated Testing

The project includes automated unit tests using **pytest** to verify:

- Root endpoint functionality
- Prediction endpoint responses
- Input validation
- Error handling behavior

Run the tests with:

```bash
pytest
```

---

# Docker Deployment

The application is containerized using Docker for reproducible deployment.

### Build the Docker image

```bash
docker build -t flight-delay-api .
```

### Run the container

```bash
docker run -p 8000:8000 flight-delay-api
```

### Access the API

```text
http://localhost:8000
```

---

# Machine Learning Workflow

1. Load trained regression model
2. Load airport encoding mappings
3. Receive HTTP request
4. Transform airport code into model-compatible features
5. Generate prediction using the trained model
6. Return prediction as a JSON response

---

# Results

The deployed API successfully:

- Serves machine learning predictions through HTTP endpoints
- Loads trained model artifacts for real-time inference
- Validates incoming requests and returns structured responses
- Passes automated unit testing with pytest
- Supports reproducible deployment using Docker containers

---

# Skills Demonstrated

- Machine Learning Deployment
- REST API Development
- FastAPI
- Docker
- Automated Testing
- Model Serving
- Python Development
- CI/CD Concepts
- MLOps Fundamentals

---

# Business Value

This project demonstrates how production-ready machine learning services can:

- Deploy predictive models through REST APIs
- Deliver real-time inference
- Support scalable application deployment
- Improve software reliability through automated testing
- Enable reproducible deployment using containerization

---

# Learning Outcomes

This project demonstrates practical experience with:

- Deploying machine learning models through APIs
- Building production-style web services
- Containerized application deployment
- Automated testing and validation
- Model inference workflows
- Reproducible deployment environments

---

# Portfolio Connection

This repository is part of a two-project portfolio demonstrating an end-to-end machine learning solution for flight delay prediction.

| Repository | Focus |
|------------|--------|
| **Flight Delay ML Pipeline** | Data engineering, feature engineering, model training, experiment tracking, and machine learning pipeline development |
| **Flight Delay API Deployment** | FastAPI application, model serving, automated testing, Docker containerization, and deployment |

Together, these projects demonstrate both machine learning development and production deployment skills.

---

# Author

**Joanna Ronchi**

- Master of Science in Data Science
- Bachelor of Science in Information Technology Management

GitHub: https://github.com/joannar77

LinkedIn: https://www.linkedin.com/in/joanna-ronchi/

---

# License

This repository is provided for portfolio and educational purposes.
