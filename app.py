# importing the libraries
from flask import Flask,render_template,request
import pickle

#Global variables
app=Flask(__name__)
loaded_model=pickle.load(open('KNN Model.pkl','rb'))

#user defined routes
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/prediction",methods=['POST'])
def predict():
    glucose=request.form['cp']
    bmi=request.form['thalach']
    age=request.form['slope']
    
    prediction=loaded_model.predict([[glucose,bmi,age]])[0]
    
    if prediction==0:
        prediction="NO HEART DISEASE"
    else:
        prediction='HAVE A HEART DISEASE'
        
    return render_template("index.html",output_prediction=prediction)


if __name__ =='__main__':
    app.run(debug=True)       


