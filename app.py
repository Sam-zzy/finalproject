from flask import Flask, render_template, request
from implementation import randorm_forest_test, random_forest_train, random_forest_predict
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random_forest import accuracy
from sklearn.metrics import accuracy_score
from time import time

app = Flask(__name__)
app.url_map.strict_slashes = False
clf, sc = None, None


@app.route('/')
def index():
    global clf, sc
    clf, sc = random_forest_train()
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def login_user():
    global clf, sc

    data_points = list()
    data = []
    string = 'value'
    for i in range(1, 31):
        value = request.form.get(string + str(i))
        # data.append(float(request.form[string + str(i)]))
        if value is None or value.strip() == "":
            return render_template('error.html')
        else:
            data.append(float(value))

    for i in range(30):
        data_points.append(data[i])

    print(data_points)
    if clf is None or sc is None:
        clf, sc = random_forest_train()

    data_np = np.asarray(data, dtype=float)
    data_np = data_np.reshape(1, -1)
    out, acc, t = random_forest_predict(clf, sc, data_np)

    if out == 1:
        output = 'Malignant'
    else:
        output = 'Benign'

    acc_x = acc[0][0]
    acc_y = acc[0][1]
    if acc_x > acc_y:
        acc1 = acc_x
    else:
        acc1 = acc_y
    return render_template('result.html', output=output, accuracy=accuracy, time=t)


if __name__ == '__main__':
    # global clf
    # clf = random_forest_train()
    randorm_forest_test(clf)
    # print("Done")
    app.run(debug=True)
