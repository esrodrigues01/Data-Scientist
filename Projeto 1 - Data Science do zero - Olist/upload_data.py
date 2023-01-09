import os
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from local_settings import postgresql as settings


postgres_connection = {
    'pguser': 'postgres',
    'pgpasswd': 'postgres',
    'pghost': 'localhost',
    'pgport': 5432,
    'pgdb': 'olist_postgres'
}

def get_engine (user,passwd, host, port, db):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url,pool_size = 50, echo = False)
    return engine

engine = get_engine(settings['pguser'], settings['pgpasswrd'], settings['pghost'], settings['pgport'], settings['pgdb'])







str_connection = 'sqlite:///{path}'


#Diretório do projeto.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Diretório dos dados
DATA_DIR = os.path.join(BASE_DIR, 'dados_csv\olist')

#Compressão de Listas
files_names = [i for i in os.listdir(DATA_DIR) if i.endswith('.csv')]

#Abrindo a conexão com o banco de dados..
str_connection = str_connection.format(path = os.path.join(DATA_DIR,'olist.db'))
connection = sqlalchemy.create_engine(str_connection)


#Conectando ao banco de dados postgres

for i in files_names:
    df_temp = pd.read_csv(os.path.join(DATA_DIR, i))
    table_name = "tb_" + i.strip(".csv").replace("olist_", "").replace("_dataset","")
    df_temp.to_sql(table_name, connection)


