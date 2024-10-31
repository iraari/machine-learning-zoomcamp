import pickle

from flask import Flask
from flask import request
from flask import jsonify

input_model = 'model1.bin'
input_dv = 'dv.bin'

with open(input_model, 'rb') as m_in: 
    model = pickle.load(m_in)

with open(input_dv, 'rb') as dv_in: 
    dv = pickle.load(dv_in)

app = Flask('subscription')

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    subscription = y_pred >= 0.5

    result = {
        'subscription_probability': float(y_pred),
        'subscription': bool(subscription)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)


'''
client = {"job": "management", 
          "duration": 400, 
          "poutcome": "success"}

client2 = {"job": "student", 
           "duration": 280, 
           "poutcome": "failure"}


print('input:', client)
print('output:', y_pred)
# output: 0.7590966516879658

client2 = {"job": "student", 
           "duration": 280, 
           "poutcome": "failure"}

X2 = dv.transform([client2])
y_pred2 = model.predict_proba(X2)[0, 1]

print('input:', client2)
print('output:', y_pred2)
#output: 0.33480703475511053
'''