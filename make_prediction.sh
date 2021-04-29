#!/usr/bin/env bash
PORT=8080
echo "Port: $PORT"
# POST method predict
curl -d '{
    "age":{
        "0":49
    },
    "sex":{
        "0":"male"
    },
    "cp":{
        "0":"non-anginal pain"
    },
    "trestbps":{
        "0":118
    },
    "chol":{
        "0":149
    },
    "fbs":{
        "0":"<120 mg/dl"
    },
    "restecg":{
        "0":"left ventricular hypertrophy"
    },
    "thalach":{
        "0": 126
    },
    "exang":{
        "0":"no"
    },
    "oldpeak":{
        "0":0.8
    },
    "slope":{
        "0":"upsloping"
    },
    "ca":{
        "0":3
    },
    "thal":{
        "0":"normal"
    }
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict