#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'

#client = {"job": "student", "duration": 280, "poutcome": "failure"}
client = {"job": "management", "duration": 400, "poutcome": "success"}

response = requests.post(url, json=client).json()
print(response)

# after 1)gunicorn running 2)05_deployment % python3 predict-test.py
# {'subscription': False, 'subscription_probability': 0.33480703475511053}

# NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, 
# currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. 
# See: https://github.com/urllib3/urllib3/issues/3020