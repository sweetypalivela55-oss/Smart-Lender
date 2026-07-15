import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model/rdf.pkl', 'rb'))

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Prediction form page
@app.route('/predict')
def predict():
    return render_template('predict.html')

# Prediction route
@app.route('/submit', methods=['POST'])
def submit():

    Gender = int(request.form['Gender'])
    Married = int(request.form['Married'])
    Dependents = int(request.form['Dependents'])
    Education = int(request.form['Education'])
    Self_Employed = int(request.form['Self_Employed'])
    ApplicantIncome = float(request.form['ApplicantIncome'])
    CoapplicantIncome = float(request.form['CoapplicantIncome'])
    LoanAmount = float(request.form['LoanAmount'])
    Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
    Credit_History = float(request.form['Credit_History'])
    Property_Area = int(request.form['Property_Area'])

    data = np.array([[Gender,
                      Married,
                      Dependents,
                      Education,
                      Self_Employed,
                      ApplicantIncome,
                      CoapplicantIncome,
                      LoanAmount,
                      Loan_Amount_Term,
                      Credit_History,
                      Property_Area]])

    prediction = int(model.predict(data)[0])

    if prediction == 1:
        result = "Loan Approved ✅"
    else:
        result = "Loan Rejected ❌"

    return render_template('submit.html', prediction=result)

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
    