## Project Title: Predictive Modeling for Insurance Premiums Based on Population Trends

Overview:

This project focuses on developing a predictive model to estimate insurance premiums based on population trends. The dataset includes key features such as age, sex, BMI (Body Mass Index), number of children, smoking status, and region. By analyzing these features, the goal is to create a model that can accurately predict insurance charges for individuals, even with limited information about them.

Dataset:

The dataset contains the following features:

Age: Age of the insured individual.
Sex: Gender of the insured individual (Male/Female).
BMI: Body Mass Index, a measure of body fat based on height and weight.
Children: Number of children/dependents covered by the insurance.
Smoker: Smoking status of the insured individual (Smoker/Non-smoker).

Target: 

Charges: The charges concerning the individual based of the features.

Usage:

1. artifacts : Data stored from the pipelines.
2. notebook : Contains the file model training which a prototype fro the model trainer
3. src: Contains everything from data ingestion to data transformation to model training and also the prediction and train pipelines
4. Components : Contains the data ingestion, data transformation, model trainer.
5. Data Ingestion: a pipeline responsable for reading the data from the source and devide it to train,test,data(raw data) and stores it in artifacts folder.
6. Data Transformation : a pipeline responsable for transforming data.
7. Model Trainer : Responsable for model training.
8. pipeline : Contains predict and train pipeline.
9. predict pipeline : Responsable for reading inputs from the UI and gives back result.
10. templates : Contains the User Interface.
11. application.py : Flask app.

Authors:

Hatim Berghaz

Acknowledgments:

Dataset link : https://www.kaggle.com/datasets/mirichoi0218/insurance
