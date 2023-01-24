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

#Selecionando nossas colunas de interesse
#Selecionado: Numero da inscrição, Nota em Matemática, Questões 1 e 2 do questinário
colunas_selecionadas_questoes = ['NU_INSCRICAO','NU_NOTA_MT', 'Q001', 'Q002', 'NU_NOTA_REDACAO']

#Criando um novo dataframe com os dados que queremos analisar
microdados_enem_selecionados = microDadosEnem.filter(items=colunas_selecionadas_questoes)
print(microdados_enem_selecionados.head())
#Removendo as linhas com NaN valores 
microdados_enem_selecionados =  microdados_enem_selecionados.dropna()

#Definindo um dicionário para melhor visualização dos dados

q001e002Dicionario = {
    'A': 'Nunca Estudou',
    'B': 'Não Completou a 4ª Série/ 5° Ano do Ensino Fundamental',
    'C': 'Completou a 4ª Série/ 5° Ano do Ensino Fundamental, mas não completou a 8ª Série/ 9° Ano do Ensino Fundamental ',
    'D': 'Completou a 8ª Série/ 9° Ano do Ensino Fundamental, mas não completou o Ensino Médio',
    'E': 'Completou o Ensino Médio, mas não completou a Faculdade',
    'F': 'Completou a Faculdade, mas não completou a Pós-Graduação',
    'G': 'Completou a Pós-Graduação',
    'H': 'Não Sei'
}

print(microdados_enem_selecionados.filter(items=['Q001', 'NU_INSCRICAO']).groupby('Q001').count())

#Criando Novas colunas no dataFrame
#vamos criar a coluna NO_Q001 no qual exibe as informações do dicionário
microdados_enem_selecionados['NO_Q001'] = [q001e002Dicionario[resp] for resp in microdados_enem_selecionados.Q001]
print(microdados_enem_selecionados.head())

#Vamos Criar a coluna NO_Q002
microdados_enem_selecionados['NO_Q002'] = [q001e002Dicionario[resp] for resp in microdados_enem_selecionados.Q002]
print(microdados_enem_selecionados.head())

#Comparando a distribuição do nível de escolaridade dos pais no conjunto de dados
#Olhando  para a escoladidade do pai 
print(microdados_enem_selecionados.filter(items=['NU_INSCRICAO', 'NO_Q001']).groupby('NO_Q001').count().sort_values(by=['NU_INSCRICAO'], ascending=False))

#Olhando agora para a escolaridade das mães
print(microdados_enem_selecionados.filter(items=['NU_INSCRICAO', 'NO_Q002']).groupby('NO_Q002').count().sort_values(by=['NU_INSCRICAO'], ascending=False))

#Respostas para as analises acima: A maior escolaridade dos pais é o Ensino médio, cerca de 683.633 pessoas seguida de não ter completado o ensino fundamental 4ª série
#Já para as mães a maior quantidade delas terminou o ensino médio e em segundo lugar completou a faculdade
#Isso demonstra que as mães tem um grau de instrução maior que os Pais

#Olhando o Desempenho em matemática seugndo a Escolaridade dos pais

#Pai
print(microdados_enem_selecionados.filter(items=['NU_NOTA_MT', 'NO_Q001']).groupby('NO_Q001').count().sort_values(by=['NU_NOTA_MT'], ascending=False))
#Resultado: Quem tira uma nota maior em matemática é filho de quem tem o ensino médio completo

#Mãe
print(microdados_enem_selecionados.filter(items=['NU_NOTA_MT', 'NO_Q002']).groupby('NO_Q002').count().sort_values(by=['NU_NOTA_MT'], ascending=False))
#Resultado: Quem tira uma nota maior em matemática é filho de quem tem o ensino médio completo

#Olhando o Desempenho em REDAÇÂO seugndo a Escolaridade dos pais

#Pai
print(microdados_enem_selecionados.filter(items=['NU_NOTA_REDACAO', 'NO_Q001']).groupby('NO_Q001').count().sort_values(by=['NU_NOTA_REDACAO'], ascending=False))
#Resultado: Quem tira uma nota maior em REDAÇÂO é filho de quem tem o ensino médio completo

#Mãe
print(microdados_enem_selecionados.filter(items=['NU_NOTA_REDACAO', 'NO_Q002']).groupby('NO_Q002').count().sort_values(by=['NU_NOTA_REDACAO'], ascending=False))
#Resultado: Quem tira uma nota maior em REDAÇÂO é filho de quem tem o ensino médio completo

print(plt.plot(colunas_selecionadas_questoes))
plt.show()