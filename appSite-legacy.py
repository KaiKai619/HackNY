from flask import Flask, render_template, request
import pickle
# Years of schooling ,english skill now (Drop down), 

app = Flask(__name__)
#model = pickle.load(open(filename, 'rb'))

@app.route('/', methods = ['GET','POST'])
def home():
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

@app.route('/api', methods=['GET','POST'])
def predict():
    #data = 
    #prediction = model.predict(data)
    #output = prediction[0]
    #return output
    return render_template('predict.html', **locals())

@app.route('/results')
def results():
    """
    Returns the results on a result page
    """
    return render_template('results.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)