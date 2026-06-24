from fastapi import FastAPI
import pickle
import json
import numpy as np

app = FastAPI()

with open("finalized_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("airport_encodings.json", "r") as f:
    airport_map = json.load(f)


def hhmm_to_seconds(hhmm: int) -> int:
    hhmm_str = f"{hhmm:04d}"
    hour = int(hhmm_str[:2])
    minute = int(hhmm_str[2:])
    return hour * 3600 + minute * 60


@app.get("/")
def root():
    return {"message": "API is functional"}


@app.get("/predict/delays")
def predict_delays(arrival_airport: str, dep_time: int, arr_time: int):
    arrival_airport = arrival_airport.upper()

    if arrival_airport not in airport_map:
        return {"error": "Airport not recognized"}

    airport_index = int(airport_map[arrival_airport])

    # Model expects: [bias] + [one-hot airport columns] + [dep_seconds, arr_seconds]
    one_hot_size = model.n_features_in_ - 3

    if airport_index >= one_hot_size:
        return {"error": "Airport not available in trained model"}

    one_hot = np.zeros(one_hot_size, dtype=float)
    one_hot[airport_index] = 1.0

    dep_seconds = hhmm_to_seconds(dep_time)
    arr_seconds = hhmm_to_seconds(arr_time)

    X = np.concatenate(([1.0], one_hot, [dep_seconds, arr_seconds])).reshape(1, -1)

    prediction = model.predict(X)
    predicted_value = float(np.ravel(prediction)[0])

    return {"predicted_departure_delay_minutes": predicted_value}