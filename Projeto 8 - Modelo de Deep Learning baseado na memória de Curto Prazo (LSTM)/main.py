import math
import yfinance as yf
import numpy as np
import pandas as pd 
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
pd.options.mode.chained_assignment = None

acao = "MGLU3.SA"
inicio = "2014-12-31"
final = "2022-09-15"

dados_acao = yf.download(acao,inicio,final)

print(dados_acao)