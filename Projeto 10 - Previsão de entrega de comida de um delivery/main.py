import pandas as pd 
import numpy as np
import plotly.express as px 
import statsmodels 
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, LSTM
import tensorflow


dados = pd.read_csv("deliverytime.txt")
#print(dados.head())
#dados.info()
#print(dados.isnull().sum())

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

#Analisando a relação entre a distância e o tempo gasto para entregar a comida:
figure = px.scatter(data_frame = dados,
                   x = "distance",
                   y = "Time_taken(min)",
                   size="Time_taken(min)",
                   trendline= "ols",
                   title="Relação entre distancia e tempo gasto")
#figure.show()

#Vejamos agora a relação entre o tempo de entrega da comida e a idade do entregador:
figure = px.scatter(data_frame = dados,
                    x = "Delivery_person_Age",
                    y = "Time_taken(min)",
                    size = "Time_taken(min)",
                    color = "distance",
                    trendline= "ols",
                    title="Relação entre Tempo de entrega e Idade"
                    )
#figure.show()

#Relação entre o tempo gasto para entregar a comida e as avaliações do entregador parceiro
figure = px.scatter(data_frame = dados,
                    x = "Delivery_person_Ratings",
                    y = "Time_taken(min)",
                    size = "Time_taken(min)",
                    color = "distance",
                    trendline= "ols",
                    title="Relação entre Tempo de entrega e Avaliações do entregador"
                    )
#figure.show()

#vejamos se o tipo de comida encomendada pelo cliente e o tipo de Moto utilizada pelo entregador parceiro influenciam ou não o tempo de entrega:

fig = px.box(dados, 
             x = "Type_of_vehicle",
             y = "Time_taken(min)",
             color = "Type_of_order")
#fig.show()

#Agora vamos treinar um modelo de Machine Learning usando um modelo de rede neural LSTM para a tarefa de previsão de tempo de entrega de comida:

#Dividindo os dados
x = np.array(dados[["Delivery_person_Age",
                    "Delivery_person_Ratings",
                    "distance"]])
y = np.array(dados[["Time_taken(min)"]])
xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size=0.10, random_state=42)

#Criando o modelo de rede neural LSTM
model = Sequential()
model.add(LSTM(128, return_sequences = True, input_shape = (xtrain.shape[1], 1)))
model.add(LSTM(64, return_sequences= False))
model.add(Dense(25))
model.add(Dense(1))
model.summary()

#Treinando o modelo 
model.compile(optimizer = 'adam', loss = 'mean_squared_error')
model.fit(xtrain, ytrain, batch_size=1, epochs=9)

#Agora vamos testar o desempenho do nosso modelo fornecendo entradas para prever o tempo de entrega da comida
print("Modelo de previsão de tempo de entrega de comida")
a = int(input("Idade do Entregador Parceiro: "))
b = float(input("Classificações de entregas anteriores: "))
c = int(input("Distancia Total: "))

features = np.array([[a,b,c]])
print("Tempo de Entrega previsto em minutos: ", model.predict(features))
