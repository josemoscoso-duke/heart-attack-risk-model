from flask import Flask, jsonify, Response, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from flask.logging import create_logger
import pandas as pd
import logging
import pickle
import urllib.request
import os

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    print(filename)
    return '.' in filename and filename.rsplit('.', 1)[1].\
                                        lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.secret_key = "secret key"

LOG = create_logger(app)
LOG.setLevel(logging.INFO)

# Load model, scaler, and column transformer
model = pickle.load(open('model/model_lr.pkl','rb'))
scaler = pickle.load(open('model/scaler.pkl','rb'))
transformer = pickle.load(open('model/column_transformer.pkl','rb'))

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

@app.route('/upload')
def upload_form():
    """upload_file"""
    print("Upload a file")
    return render_template('upload.html')

@app.route('/upload', methods=['GET','POST'])
def upload_file():
    if (request.method == 'POST') or (request.method == 'GET') :
        print('inside POST')        
    # check if the post request has the file part
        if 'file' not in request.files:
            print('inside file not in request')
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('inside file empty')
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            print('Im here allowed file')
            filename = secure_filename(file.filename)
            flash('filename')
            file.save(os.path.join('data', filename))
            flash('File successfully uploaded')
            return redirect('/')
        else:
            flash('Allowed file type is csv')
            return redirect(request.url)


@app.route('/echo/<name>')
def echo(name):
    print(f"This was placed in the url: new-{name}")
    val = {"new-name": name}
    return jsonify(val)

@app.route('/predict', methods = ['GET','POST'])
# Make prediction
def predict():
    #json_payload = request.json
    #LOG.info(f"JSON payload: {json_payload}")
    data = pd.read_csv(os.path.join('data', 'csv_test.csv'))
    LOG.info(f"inference payload DataFrame: {data}")
    prediction = make_prediction(model, data, scaler, transformer)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)