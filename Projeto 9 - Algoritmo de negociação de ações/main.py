import pandas as pd 
import plotly.graph_objects as go
from plotly._subplots import make_subplots
import plotly.express as px 
import yfinance as yf

#Obtendo dados das ações da Apple no yahoo finance
stock = yf.Ticker("PETR4.SA")
data = stock.history(period = "1y")
#print(data.head())

#Calculadora de momento 
data['momentum'] = data['Close'].pct_change()

#Criando subplots para exibir o momento e compra/venda 
figure = make_subplots(rows=2, cols=1)
figure.add_trace(go.Scatter(x = data.index, y=data['Close'], name='Preço de Fechamento'))
figure.add_trace(go.Scatter(x=data.index, y= data['momentum'], name='Momento', yaxis='y2'))

#Adicionando sinais de COMPRA e VENDA 
figure.add_trace(go.Scatter(x = data.loc[data['momentum'] > 0 ].index, y= data.loc[data['momentum'] > 0] ['Close'], mode='markers', name = 'Compra', marker=dict(color='green', symbol = 'triangle-up')))

figure.add_trace(go.Scatter(x = data.loc[data['momentum'] < 0 ].index, y= data.loc[data['momentum'] < 0] ['Close'], mode='markers', name = 'Venda', marker=dict(color='red', symbol = 'triangle-down')))

figure.update_layout(title = 'Algoritmo de negociação usando a estratégia do momento', xaxis_title = 'Data', yaxis_title = 'Preço')
figure.update_yaxes(title = "Momentum", secondary_y = True)
figure.show()