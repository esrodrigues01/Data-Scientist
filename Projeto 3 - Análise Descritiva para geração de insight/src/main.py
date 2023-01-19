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