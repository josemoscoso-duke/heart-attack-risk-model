import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    #wait_time = between(1, 2.5)

    @task
    def submitForm(self):
        self.client.post("/predict", json = {"age":{"0":49},
                                             "sex":{"0":"Male"},
                                             "cp":{"0":"Non-anginal pain"},
                                             "trestbps":{"0":118},
                                             "chol":{"0":149},
                                             "fbs":{"0":"<120 mg/dl"},
                                             "restecg":{"0":"Left ventricular hypertrophy"},
                                             "thalach":{"0": 126},
                                             "exang":{"0":"No"},
                                             "oldpeak":{"0":0.8},
                                             "slope":{"0":"Upsloping"},
                                             "ca":{"0":3},
                                             "thal":{"0":"Normal"}
                                            })

# class WebsiteUser(HttpUser):
#     wait_time = between(1, 7)
    
    
#     @task
#     def index(self):
#         self.client.get("/")
    
        
#     @task
#     def pred(self):
#         self.client.post("/predict", { "age":49 ,  "sex": "Male", "cp":"Non-anginal pain", "trestbps":118, "chol":149, "fbs":"<120 mg/dl", "restecg":"Left ventricular hypertrophy", "thalach": 126, "exang":"No", "oldpeak" : 0.8, "slope":"Upsloping",  "ca": 3, "thal":"Normal"})






