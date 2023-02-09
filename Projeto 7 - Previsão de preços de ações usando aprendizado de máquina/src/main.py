import numpy as np
import pandas as pd
from sklearn import preprocessing 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 

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

#ler os dados 
df = pd.read_csv("data\MSFT.csv")
df = df[df.symbol == "MSFT"]