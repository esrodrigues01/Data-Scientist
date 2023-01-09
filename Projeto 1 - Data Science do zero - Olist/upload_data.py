import psycopg2

host = 'localhost'
dbname = 'olistdb'
user = 'postgres'
password = 'postgres'


#string de conexão
conn_string = 'host={0} user={1} dbname={2} password={3}'.format(host,user,dbname,password)

print(conn_string)

conn = psycopg2.connect(conn_string)
print("Sucesso")
