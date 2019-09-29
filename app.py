from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pandas as pd


data = pd.read_csv("Cleaned_ASR_Data.csv")

X = data[['Years_of_Schooling', 'English_Skill_Now']]
y = data['Income_Per_Hour']

income_regression = LinearRegression().fit(X, y)


@app.route('/')
def hello_world():
    """
    Home page, takes input data from html form and then predicts
    """
    
    # extract Form input data
    #formData = formData

    #schoolYears = formData[0]
    #englishSkill = formData[1]
    #country = formData[2]
    #gender = formData[3]

    #prediction = model.predict(data)
    return render_template('example.html', **locals())
