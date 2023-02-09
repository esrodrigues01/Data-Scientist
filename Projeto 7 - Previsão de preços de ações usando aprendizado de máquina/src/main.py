import numpy as np
import pandas as pd
from sklearn import preprocessing 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
import os

##Lendo os dados CSV que estão na pasta dados
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR,'data')
files_names  = [i for i in os.listdir(DATA_DIR) if i.endswith('.csv')]
for i in files_names:
    df = pd.read_csv(os.path.join(DATA_DIR,i),sep=",", encoding="ISO-8859-1")


#preparação dos dados 
def prepare_data(df,forecast_col,forecast_out,test_size):
    label = df[forecast_col].shift(-forecast_out) #creating new column called label with the last 5 rows are nan
    X = np.array(df[[forecast_col]]) #creating the feature array
    X = preprocessing.scale(X) #processing the feature array
    X_lately = X[-forecast_out:] #creating the column i want to use later in the predicting method
    X = X[:-forecast_out] # X that will contain the training and testing
    label.dropna(inplace=True) #dropping na values
    y = np.array(label)  # assigning Y
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=test_size, random_state=0) #cross validation

    response = [X_train,X_test , Y_train, Y_test , X_lately]
    return response


forecast_col = 'Close'
forecast_out = '300'
test_size = 0.2

x_train, x_test, y_train, y_test, x_lately = prepare_data(df,forecast_col,forecast_out, test_size);
learner = LinearRegression()

learner.fit(x_train, y_train)


score = learner.score(x_test, y_test)
forecast = learner.predict(x_lately)
response = {}
response['test_score'] = score
response['forecast_set'] = forecast

print(response)
