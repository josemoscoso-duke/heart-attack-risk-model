from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(1, 7)
    
    
    @task
    def index(self):
        self.client.get("/")
    
        
    @task
    def pred(self):
        self.client.post("/predict", { "age":49 ,  "sex": "Male", "cp":"Non-anginal pain", "trestbps":118, "chol":149, "fbs":"<120 mg/dl", "restecg":"Left ventricular hypertrophy", "thalach": 126, "exang":"No", "oldpeak" : 0.8, "slope":"Upsloping",  "ca": 3, "thal":"Normal"})





