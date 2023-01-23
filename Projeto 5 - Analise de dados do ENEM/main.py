import os
import pandas as pd


##Lendo os dados CSV que estão na pasta dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR,'dados')
files_names  = [i for i in os.listdir(DATA_DIR) if i.endswith('.csv')]
for i in files_names:
    microDadosEnem = pd.read_csv(os.path.join(DATA_DIR,i),sep=";", encoding="ISO-8859-1")
print(microDadosEnem.head())
print(microDadosEnem)