--Codigo ultilizado no googleBigQuery

--Selecionando uma lista com os nomes e os cpf dos candidatos a governador de Mato Grosso
SELECT DISTINCT
 nome_candidato,
 cpf_candidato 
FROM `basedosdados.br_tse_eleicoes.receitas_candidato`
WHERE ano = 2018 
and sigla_uf = 'MT' 
and cargo = 'governador'

--Mostrando o valor máximo, o minimo, a média e a soma total das receita doadas durante a campanha de 2018

SELECT 
  MAX(valor_receita) as maximo,
  MIN(valor_receita) as minimo,
  AVG(valor_receita) as media,
  SUM(valor_receita) as soma
FROM `basedosdados.br_tse_eleicoes.receitas_candidato` 
WHERE ano = 2018 AND sigla_uf = 'MT'
LIMIT 100

--Mostrando a quantidade de doadores (CPF e CNPJ) de campanhas no Estado de MT 
SELECT 
  count(distinct cpf_cnpj_doador) as QTD_DOADORES_DISTINTOS
from `basedosdados.br_tse_eleicoes.receitas_candidato` 
where ano = 2018 and sigla_uf = 'MT' 