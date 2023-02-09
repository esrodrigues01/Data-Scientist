import numpy as np
import pandas as pd
from sklearn import preprocessing 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
import os

#preparação dos dados 
def prepare_data(df,forecast_col, forecast_out, test_size):
    label = df[forecast_col].shift(-forecast_out) #Criando nova coluna Label; ultimas 5 linhas são NaN
    x = np.array(df[[forecast_col]]) #Criado a matriz de recursos
    x = preprocessing.scale(x)
    x_lately = x[-forecast_out:]
    label.dropna(inplace = True)
    y = np.array(label)
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = test_size, random_state = 0)

    response = [x_train, x_test, y_train, y_test, x_lately]

    return response

##Lendo os dados CSV que estão na pasta dados
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR,'data')
files_names  = [i for i in os.listdir(DATA_DIR) if i.endswith('.csv')]
for i in files_names:
    microDadosEnem = pd.read_csv(os.path.join(DATA_DIR,i),sep=",", encoding="ISO-8859-1")

print (microDadosEnem)

