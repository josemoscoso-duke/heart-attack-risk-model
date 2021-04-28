#!/usr/bin/env bash

PORT=8080
echo "Port: $PORT"

# POST method predict
curl -d '{
    "age":{
        "0":"35"
    },
    "sex":{
        "0":"female"
    },
    "cp":{
        "0":"non-anginal pain"
    },
    "trestbps":{
        "0":"145"
    },
    "chol":{
        "0":"200"
    },
    "fbs":{
        "0":"<120 mg/dl"
    },
    "restecg":{
        "0":"normal"
    },
    "thalach":{
        "0":"160"
    },
    "exang":{
        "0":"yes"
    },
    "oldpeak":{
        "0":"1.0"
    },
    "slope":{
        "0":"flat"
    },
    "ca":{
        "0":"0"
    },
    "thal":{
        "0":"normal"
    }
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict