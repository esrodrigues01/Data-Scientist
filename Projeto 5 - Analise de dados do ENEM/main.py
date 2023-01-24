import os
import pandas as pd
import matplotlib as mt
import matplotlib.pyplot as plt
import numpy as np


##Lendo os dados CSV que estão na pasta dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR,'dados')
files_names  = [i for i in os.listdir(DATA_DIR) if i.endswith('.csv')]
for i in files_names:
    microDadosEnem = pd.read_csv(os.path.join(DATA_DIR,i),sep=";", encoding="ISO-8859-1")


#Começando a análise exploratória
#print(microDadosEnem.columns.values)
colunas_selecionadas_enem = ['TP_FAIXA_ETARIA' ,'TP_SEXO' ,'TP_ESTADO_CIVIL',
 'TP_COR_RACA' ,'TP_NACIONALIDADE' ,'TP_ST_CONCLUSAO', 'TP_ANO_CONCLUIU',
 'TP_ESCOLA' ,'TP_ENSINO' ,'IN_TREINEIRO' ,'CO_MUNICIPIO_ESC',
 'NO_MUNICIPIO_ESC' ,'CO_UF_ESC', 'SG_UF_ESC', 'TP_DEPENDENCIA_ADM_ESC',
 'TP_LOCALIZACAO_ESC', 'TP_SIT_FUNC_ESC', 'CO_MUNICIPIO_PROVA',
 'NO_MUNICIPIO_PROVA', 'CO_UF_PROVA' ,'SG_UF_PROVA', 'TP_PRESENCA_CN',
 'TP_PRESENCA_CH', 'TP_PRESENCA_LC', 'TP_PRESENCA_MT', 'CO_PROVA_CN',
 'CO_PROVA_CH', 'CO_PROVA_LC' ,'CO_PROVA_MT' ,'NU_NOTA_CN' ,'NU_NOTA_CH',
 'NU_NOTA_LC', 'NU_NOTA_MT' ,'TX_RESPOSTAS_CN' ,'TX_RESPOSTAS_CH',
 'TX_RESPOSTAS_LC', 'TX_RESPOSTAS_MT', 'TP_LINGUA', 'TX_GABARITO_CN',
 'TX_GABARITO_CH' ,'TX_GABARITO_LC' ,'TX_GABARITO_MT' ,'TP_STATUS_REDACAO',
 'NU_NOTA_COMP1' ,'NU_NOTA_COMP2' ,'NU_NOTA_COMP3','NU_NOTA_COMP4',
 'NU_NOTA_COMP5', 'NU_NOTA_REDACAO']

microdados_enem_selecionados = microDadosEnem.filter(items=colunas_selecionadas_enem)
#print(microdados_enem_selecionados.head())

#Visualizando por faixa etária
coluna_faixa_etaria =  microdados_enem_selecionados['TP_FAIXA_ETARIA']
#Mostrando na tela ordenados as faixas de idade com mais inscritos 
print(coluna_faixa_etaria.value_counts().sort_index())
print(plt.hist(coluna_faixa_etaria, bins=30))
plt.show()
#Olhando para quantos alunos fizeram a prova do ENEM por Estados 
coluna_estados = microdados_enem_selecionados['SG_UF_PROVA']
print(coluna_estados.value_counts())
print(plt.hist(coluna_estados, bins=30))
plt.show()

#Respondendo Questões levantadas no codigo acima: 
# 1 - Qual é a faixa etária em que mais alunos fizeram o ENEM?
# Resposta 1: FAIXA 3: 18 ANOS 
# 2 - Qual o Estado Brasileiro com mais incritos na prova do ENEM?
# Resposta 2: SÃO PAULO (SP) COM 509.954 INSCRIÇOES

#Codigo abaixo se refere a descobrirmos qual sexo teve as melhores notas na redação do ENEM
colunas_selecionadas = ['NU_NOTA_REDACAO', 'TP_SEXO']
microdados_sexo_redacao = microDadosEnem.filter(items=colunas_selecionadas)
#print(microdados_sexo_redacao.head())
#limpando os valores NaN da variáve NU_NOTA_REDACAO
microdados_sexo_redacao = microdados_sexo_redacao.dropna()
print(microdados_sexo_redacao.head())
print(microdados_sexo_redacao.groupby('TP_SEXO').count())
print(microdados_sexo_redacao.groupby('TP_SEXO').max())
#Abaixo Mostrando as notas minimas maiores que 0  de ambos os sexos
print(microdados_sexo_redacao[microdados_sexo_redacao.NU_NOTA_REDACAO > 0].groupby('TP_SEXO').min())
#Abaixo Mostrando as médias das notas da redaçao por sexo no ENEM
print(microdados_sexo_redacao.groupby('TP_SEXO').mean())
#Abaixo Mostrando a mediana das notas da redaçao por sexo no ENEM
print(microdados_sexo_redacao.groupby('TP_SEXO').median())
#Plotar gráfico para melhor visualização
print(microdados_sexo_redacao.groupby('TP_SEXO').hist(bins=30))
plt.show()
#Mostrando um método mais completo para visualizar os dados; describe(), ele nos fornece uma noção do conjunto de dados. 
#Fornece: Contagem, Média, Desvio Padrão, minimo, distribuição por quartiz, e o máximo
print(microdados_sexo_redacao.groupby('TP_SEXO').describe())

#Respondendo Questões levantadas no codigo acima: 
# As notas da redação em relação ao sexo do candidato. O sexo do candidato não tem muita influencia, as diferenças são bem sutis nos dados e gráficos
#Uma ideia é observaar a nota da redação com os indicadores socioeconomicos dos candidados, teremos uma resposta mais fiel a realidade
