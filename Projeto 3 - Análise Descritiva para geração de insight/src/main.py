import numpy as np
import pandas as pd 
import os


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
