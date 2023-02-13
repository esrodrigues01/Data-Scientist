import pandas as pd 
import plotly.graph_objects as go
from plotly._subplots import make_subplots
import plotly.express as px 
import yfinance as yf

#Obtendo dados das ações da Apple no yahoo finance
stock = yf.Ticker("AAPL")
data = stock.history(period = "1y")
print(data.head())

#Calculadora de momento 
data['momentum'] = data['Close'].pct_change()

#Criando subplots para exibir o momento e compra/venda 
figure = make_subplots(rows=2, cols=1)
figure.add_trace(go.Scatter(x = data.index, y=data['Close'], name='Close Price'))
figure.add_trace(go.Scatter(x=data.index, y= data['momentum'], name='Momentum', yaxis='y2'))

#Adicionando sinais de COMPRA e VENDA 
