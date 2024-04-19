from flask import Flask,request,render_template
import sys
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
from src.pipeline.train_pipeline import trainPipeline

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            age = request.form.get('age'),
            sex=request.form.get('sex'),
            bmi=request.form.get('bmi'),
            children=request.form.get('children'),
            smoker=request.form.get('smoker'),
            region=request.form.get('region'),
        )
        
        userinput = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()
        trainingPipeline = trainPipeline()
        trainingPipeline.training(userinput)
        results = predict_pipeline.predict(userinput)
        return render_template('home.html',results = results[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)