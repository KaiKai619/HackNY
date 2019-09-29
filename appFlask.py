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


@app.route('/', methods=['POST'])
def hello_world():
    """
    Home page, takes input data from html form and then predicts
    """

    #prediction = model.predict(data)
    return render_template('example.html', **locals())
