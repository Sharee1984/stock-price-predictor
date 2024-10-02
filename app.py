from flask import Flask,render_template,jsonify
import pickle
import numpy as np
from flask import request

model = pickle.load(open('modelA.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict_price():
    Open = float(request.form.get('Open'))
    High = float(request.form.get('High'))
    Low = float(request.form.get('Low'))
    Pre_Close = float(request.form.get('Pre_Close'))

    # Prediction
    input_query = np.array([[Open,High,Low,Pre_Close]])

    result = model.predict(input_query)
    return str(round(result[0],2))




if __name__ == '__main__':
    app.run(debug=True)

