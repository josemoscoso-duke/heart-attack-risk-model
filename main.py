from flask import Flask
from flask import jsonify
import logging
import pickle


logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
# Load model, scaler, and column transformer
model = pickle.load(open('model/model_lr.pkl'.'rb'))
scaler = pickle.load(open('model/scaler.pkl'.'rb'))
transformer = pickle.load(open('model/column_transformer.pkl'.'rb'))

def make_prediction(model, data, scaler, transformer):    
    x_new = data.values
    
    # Set categorical and numerical columns
    categorical_cols = [1, 2, 5, 6, 8, 10, 12]
    numerical_cols = [0, 3, 4, 7, 9, 11]
    
    x_new[:, numerical_cols] = scaler.transform(x_new[:, numerical_cols])
    x_new = transformer.transform(x_new)
    
    # Make prediction
    new_preds = model.predict(x_new)
    
    new_preds = ['Not at Risk' if pred == 0 else 'At Risk' for pred in new_preds]
    
    return new_preds

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World! CD'

@app.route('/echo/<name>')
def echo(name):
    print(f"This was placed in the url: new-{name}")
    val = {"new-name": name}
    return jsonify(val)

@app.route('/predict', methods = ['POST'])
# Make prediction
def predict():
    json_payload = request.json
    LOG.info(f"JSON payload: {json_payload}")
    data = pd.DataFrame(json_payload)
    LOG.info(f"inference payload DataFrame: {inference_payload}")
    prediction = make_prediction(model, data, scaler, transformer)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)