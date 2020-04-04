import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


from flask import Flask,jsonify,request, render_template


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/")

def home():
  return render_template('index.html')

# This function to convert prediction values to LOW or HIGH
def convert(x):
    if x==0:
        return("LOW")
    else:
        return("HIGH")

@app.route("/predict",methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    # Convert 0 or 1 to LOW or HIGH
    result= convert(prediction)
    return render_template('index.html', prediction_text ="Stroke probability is {}".format(result))



if __name__ == "__main__":
    app.run(debug=True) 


