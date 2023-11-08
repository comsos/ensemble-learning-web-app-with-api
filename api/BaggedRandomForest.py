from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
import pickle
from flask import Flask, request
import json
import joblib
from flask_cors import CORS

loaded_model = joblib.load('model.sav')

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"/*": {"origins": "*"}}) 

@app.route('/predict', methods = ['POST'])
def prediction_model():
  data = request.get_json()

  td = data['array']

  arr = []
  for i in td:
    arr.append(i)

  result = loaded_model.predict([arr]) 

  print(result)

  return json.dumps({"result":result[0]}) 

if __name__ == "__main__":
  app.run(port=5000, debug=True)
