import json
import numpy as np 
import pandas as pd 
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error

from statsmodels.tsa.stattools import adfuller
from scipy import stats
from scipy.stats import normaltest
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from flask import Flask, render_template, request
app = Flask(__name__)


import warnings
warnings.filterwarnings("ignore")


@app.route('/', methods=['GET', 'POST'])
def index():
    flag = False
    if request.method == 'GET':
        flag = True
        return render_template('index.html',flag=flag)

    elif request.method == 'POST':
        flag=False
        file_name = request.form['ticker']
        data = pd.read_csv(file_name)
        # data = pd.read_csv('abc.csv')

        data['Close'] = data['Close'] * 1.0
        close_1 = data['Close']
        c = '#386B7F'


        train_data, test_data = data[0:int(len(data)*0.7)], data[int(len(data)*0.7):]
        training_data = train_data['Close'].values
        test_data = test_data['Close'].values

        history_of_train = [x for x in training_data]
        predictions = []
        test_records = len(test_data)
        for times in range(test_records):
            sarima = SARIMAX(history_of_train, order=(4,4,0))
            sarima_fit = sarima.fit(disp=0)
            output = sarima_fit.forecast()
            pred = output[0]
            predictions.append(pred)
            test_value = test_data[times]
            history_of_train.append(test_value)

        sarima_test_MAE=mean_absolute_error(test_data, predictions)
        mae=round(sarima_test_MAE,3)

        Sarima = SARIMAX(data['Close'],order=(4,1,0),seasonal_order=(1,1,1,12),enforce_invertibility=False, enforce_stationarity=False)
        Sarima = Sarima.fit()
        predictions = Sarima.predict(start=len(data), end= len(data)+42, dynamic= True)
        p_dict = {}
        i = 0
        for k, v in predictions.items():
            i += 1
            p_dict[i] = v
        return render_template('index.html', predictions=p_dict, mae=mae,flag=flag,name=file_name.split(".csv"))


if __name__ == '__main__':
    app.run()
