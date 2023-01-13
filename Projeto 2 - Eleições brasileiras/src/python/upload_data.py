import os 
import pandas as pd

BASE_DIR = (os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
DATA_DIR = os.path.join(BASE_DIR,'data')

files_names = [i for i in os.listdir(DATA_DIR) if i.endswith('.csv')]

for i in files_names:
    df_tmp = pd.read_csv(os.path.join(DATA_DIR,i))


