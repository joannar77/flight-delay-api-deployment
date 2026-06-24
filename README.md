# Flight Delay Prediction REST API

## FastAPI-Based Machine Learning Model Deployment

A production-style REST API developed to deploy a trained machine learning model for flight delay prediction. The application exposes prediction endpoints through FastAPI, incorporates automated testing with pytest, and supports containerized deployment using Docker.

---

## Project Overview

This project demonstrates the deployment phase of the machine learning lifecycle by transforming a trained predictive model into an accessible web service.

The API accepts flight-related inputs, processes requests using a trained regression model, and returns predicted departure delays through HTTP endpoints.

---

## Technologies Used

### Backend Development

- Python
- FastAPI
- Uvicorn

### Machine Learning

- Scikit-learn
- NumPy
- Pandas

### Testing

- Pytest

### Deployment

- Docker

### Version Control

- Git
- GitHub

---

## Features

- REST API endpoint for flight delay prediction
- JSON-based request and response handling
- Automated unit testing
- Docker containerization
- Machine learning model deployment
- Airport code encoding support
- HTTP endpoint validation

---

## Project Architecture

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

## API Endpoints

### Root Endpoint

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

### Delay Prediction Endpoint

```http
GET /predict/delays
```

Accepts:

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

## Automated Testing

The project includes automated unit tests using pytest to verify:

- Root endpoint functionality
- Prediction endpoint responses
- Input validation
- Error handling behavior

Run tests with:

```bash
pytest
```

---

## Docker Deployment

The application is containerized using Docker for reproducible deployment.

Build image:

```bash
docker build -t flight-delay-api .
```

Run container:

```bash
docker run -p 8000:8000 flight-delay-api
```

Access API:

```text
http://localhost:8000
```

---

## Machine Learning Workflow

1. Load trained regression model
2. Load airport encoding mappings
3. Receive HTTP request
4. Transform airport code into model-compatible features
5. Generate prediction using the trained model
6. Return prediction as a JSON response

---

## Results

The deployed API successfully:

- Serves machine learning predictions through HTTP endpoints
- Loads trained model artifacts for real-time inference
- Validates incoming requests and returns structured responses
- Passes automated unit testing with pytest
- Supports reproducible deployment using Docker containers

---

## Key Skills Demonstrated

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

## Learning Outcomes

This project demonstrates practical experience with:

- Deploying machine learning models through APIs
- Building production-style web services
- Containerized application deployment
- Automated testing and validation
- Model inference workflows
- Reproducible deployment environments

---

## Project Portfolio Connection

This repository is part of a two-project portfolio demonstrating an end-to-end machine learning solution for flight delay prediction.

| Repository | Focus |
|------------|--------|
| [Flight Delay ML Pipeline](https://github.com/joannar77/flight-delay-ml-pipeline) | Data engineering, feature engineering, model training, experiment tracking, and machine learning pipeline development |
| [Flight Delay API Deployment](https://github.com/joannar77/flight-delay-api-deployment) | FastAPI application, model serving, automated testing, Docker containerization, and deployment |

Together, these projects demonstrate both machine learning development and production deployment skills.

## Author

**Joanna Ronchi**

Master of Science, Data Analytics (Data Science Specialization)

GitHub: https://github.com/joannar77

LinkedIn: https://www.linkedin.com/in/joanna-ronchi/

---

## License

This repository is provided for portfolio and educational purposes.
