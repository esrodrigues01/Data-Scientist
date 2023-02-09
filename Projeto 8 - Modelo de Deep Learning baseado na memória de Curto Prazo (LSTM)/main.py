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

#pegando cotações de fechamento 

cotacao_fechamento = dados_acao['Close'].to_numpy().reshape(-1,1)

#print(cotacao_fechamento)

#treinando 80% dos dados e 20% do teste
tamanho_dados_treinamento =  int(len(cotacao_fechamento) * 0.8)

#print(tamanho_dados_treinamento)

#Escalar os dados 
escalador = MinMaxScaler(feature_range=(0,1))
dados_entre01_treinamento = escalador.fit_transform(cotacao_fechamento[0: tamanho_dados_treinamento, :])
dados_entre01_teste = escalador.transform(cotacao_fechamento[tamanho_dados_treinamento:,:])

dados_entre01 = list(dados_entre01_treinamento.reshape(
    len(dados_entre01_treinamento))) + list(dados_entre01_teste.reshape(
    len(dados_entre01_teste)))
dados_entre01 = np.array(dados_entre01).reshape(len(dados_entre01), 1)

print(dados_entre01)