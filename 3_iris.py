from flask import Flask,request,render_template,jsonify
import pickle
import numpy as np
import dataclasses

with open('model.pkl','rb') as f:
    model = pickle.load(f)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('2_iris_data.html')


@app.route('/iris',methods=['POST'])
def predict():
    SepalLengthCm = float(request.form['sl'])
    SepalWidthCm = float(request.form['sw'])
    PetalLengthCm = float(request.form['pl'])
    PetalWidthCm = float(request.form['pw'])
    
    data = np.array([SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm],ndmin=2)
    result = model.predict(data)

    print(result)


    if result[0] == 0:
        pred = 'Iris-setosa'

    if result[0] == 1:
        pred = 'Iris-versicolor'

    if result[0] == 2:
        pred = 'Iris-virginica'
       
    return jsonify(pred)


    


if __name__ == "__main__":
    app.run(debug=True)