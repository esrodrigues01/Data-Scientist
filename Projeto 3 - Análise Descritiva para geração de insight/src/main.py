import numpy as np
import pandas as pd 
import os
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt


##Lendo os dados CSV que estão na pasta dados
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR,'dados')
files_names  = [i for i in os.listdir(DATA_DIR) if i.endswith('.csv')]
for i in files_names:
    df = pd.read_csv(os.path.join(DATA_DIR,i))

#Explorando o conjunto de dados
print(df.info)
print(df.isnull().sum())

#Tratando dados ausentes, incorreto ou inválido

#Substituindo %, "," e "-" por " "
df = df.replace('%','',regex=True)
df = df.replace(',','',regex=True)
df = df.replace('-','',regex=True)
df = df.replace('', np.nan)
df = df.replace('MAY90', np.nan)

#Removendo Linhas com valores NaN  
df = df.dropna()

#Checando se todos os valores NaN foram resolvidos
print(df.isnull().sum())

#Convertendo tipos de dados para float
lista = ["Coarse wool Price", "Coarse wool price % Change", "Copra Price", "Copra price % Change", "Cotton Price", "Cotton price % Change", "Fine wool Price", "Fine wool price % Change", "Hard log Price", 
        "Hard log price % Change", "Hard sawnwood Price", "Hard sawnwood price % Change", "Hide Price", "Hide price % change", "Plywood Price", "Plywood price % Change", "Rubber Price",
         "Rubber price % Change", "Softlog Price", "Softlog price % Change", "Soft sawnwood Price", "Soft sawnwood price % Change",
         "Wood pulp Price", "Wood pulp price % Change"]
df[lista] = df[lista].astype("float")
print(df.dtypes)
print(df.head())


#Formatando a coluna datetime e definindo como indice para o conjunto de dados
df.Month = pd.to_datetime(df.Month.str.upper(), format='%b%y', yearfirst=False)
df = df.set_index('Month')
print(df.head())


#Começando a análise exploratória
#Usaremos a biblioteca matplotlib.pyolot e seaborn

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9 , 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'


#Mapa de Calor
#Lista de raw_material
raw_data =["Coarse wool Price",  "Copra Price",  "Cotton Price",  "Fine wool Price", "Hard log Price", 
         "Hard sawnwood Price",  "Hide Price",  "Plywood Price",  "Rubber Price", "Softlog Price",  "Soft sawnwood Price", 
         "Wood pulp Price"]

#fazendo a matriz de correlação
corrmat = df[raw_data].corr()

#Configurando o tamanho e plotando
fig = plt.figure(figsize=(12,9))

#mascarando a parte triangular superior, pois a matriz é simétrica (repetitiva)
mask =  np.triu(np.ones_like(corrmat,dtype = bool))
sns.heatmap(corrmat,vmax= .8, mask = mask, square= True, annot=True)
plt.show()


