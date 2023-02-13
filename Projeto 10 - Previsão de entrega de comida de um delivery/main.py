import pandas as pd 
import numpy as np
import plotly.express as px 
import statsmodels 

dados = pd.read_csv("deliverytime.txt")
#print(dados.head())
#dados.info()
print(dados.isnull().sum())

# R = Raio do planeta Terra 
R = 6371

#Função que converte degraus para radianos
def deg_to_rad(degrees):
    return degrees * (np.pi/180)

#Função para calcular distancia entre dois pontos usando haversine 
def distCalcular(lat1, lon1, lat2, lon2):
    d_lat = deg_to_rad(lat2 - lat1)
    l_long = deg_to_rad(lon2 - lon1)
    a = np.sin(d_lat/2)**2 + np.cos(deg_to_rad(lat1)) * np.cos(deg_to_rad(lat2)) * np.sin(l_long/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return R * c

#Função para calcular a distancia entre cada par de pontos 
dados['distance'] = np.nan

for i in range(len(dados)):
    dados.loc[i,'distance'] = distCalcular(dados.loc[i,'Restaurant_latitude'],
                                           dados.loc[i,'Restaurant_longitude'],
                                           dados.loc[i,'Delivery_location_latitude'],
                                           dados.loc[i,'Delivery_location_longitude'])

#print(dados.head())

#Desenvolvendo a exploração de dados 

figure = px.scatter(data_frame = dados,
                    x = "distance",
                    y = "Time_taken(min)",
                    size="Time_taken(min)",
                    trendline= "ols",
                    title="Relação entre distancia e tempo gasto")
figure.show()