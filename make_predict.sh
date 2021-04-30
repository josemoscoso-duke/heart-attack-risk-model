#!/usr/bin/env bash

# POST method predict
curl -d '{
    "age":49,
    "sex":"Male",
    "cp":"Non-anginal pain",
    "trestbps":118,
    "chol":149,
    "fbs":"<120 mg/dl",
    "restecg":"Left ventricular hypertrophy",
    "thalach":126,
    "exang":"No",
    "oldpeak":0.8,
    "slope":"Upsloping",
    "ca":3,
    "thal":"Normal"
}'\
     -H "Content-Type: application/json" \
     -X POST https://cloud-final-project-311921.uc.r.appspot.com/predict