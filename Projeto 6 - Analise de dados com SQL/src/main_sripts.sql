select
	ano,
	trial_cargo_5,
	trial_sigla_partido_22 
from microdados m 
where trial_nome_municipio_4 = 'Várzea Grande'

--Remover Repetições de dados 
select
	distinct instituto 
from microdados m 

--Olhando para dados das pesquisas do DATAFOLHA ou Ibope a partir de 2014 no estado de Mato Grosso
select
	 * 
from microdados m 
where (instituto = 'Datafolha' or instituto = 'Ibope') and (ano > 2013) and (sigla_uf = 'MT')

--Descobrir as siglas de partidos distintos que concorreram nas eleições a partir de 2014
--Detalhe que limpamos os campos que tinha n/a entre outros dados incorretos.
select
	distinct trial_sigla_partido_22  
from microdados m 
where ano between 2014 and 2020
and (trial_sigla_partido_22 != 'sem partido' 
and trial_sigla_partido_22 != 'N/A' 
and trial_sigla_partido_22 != '* ' 
and trial_sigla_partido_22 != '* T'
and trial_sigla_partido_22 != '* TR'
and trial_sigla_partido_22 != '* TRIA'
and trial_sigla_partido_22 != '* TRIAL'
and trial_sigla_partido_22 != '* TRIAL '
and trial_sigla_partido_22 != '* TRIAL *'
and trial_sigla_partido_22 != '* TRIAL * T'
and trial_sigla_partido_22 != '* TRIAL * TR'
and trial_sigla_partido_22 != '* TRIAL * TRI')
order by trial_sigla_partido_22;

-- Limpando dados NULL e * das pesquisas 
select 
	*
from microdados m 
where instituto in ('Datafolha', 'Ibope') 
and sigla_uf is not null 
and sigla_uf != '* '
order by sigla_uf 

--Respondendo ao questionamento de consultar todas as pesquisas eleitorais realizadas em 2018 para presidente ordenando por turno
--Limpando os dados com inconsistencias
select 
	distinct id_pesquisa, 
	ano, 
	trial_cargo_5,
	trial_turno_16, 
	data_referencia, 
	instituto
from microdados m  
where ano = 2018 
and trial_cargo_5 = 'presidente'
and trial_cargo_5 != 'N/A' 
and trial_cargo_5 != '* ' 
and trial_cargo_5 != '* T'
and trial_cargo_5 != '* TR'
and trial_cargo_5 != '* TRIA'
and trial_cargo_5 != '* TRIAL'
and trial_cargo_5 != '* TRIAL '
and trial_cargo_5 != '* TRIAL *'
and trial_cargo_5 != '* TRIAL * T'
and trial_cargo_5 != '* TRIAL * TR'
and trial_cargo_5 != '* TRIAL * TRI'
and instituto != 'N/A' 
and instituto != '* ' 
and instituto != '* T'
and instituto != '* TR'
and instituto != '* TRI'
and instituto != '* TRIA'
and instituto != '* TRIAL'
and instituto != '* TRIAL '
and instituto != '* TRIAL *'
and instituto != '* TRIAL * '
and instituto != '* TRIAL * T'
and instituto != '* TRIAL * TR'
and instituto != '* TRIAL * TRIAL '
and instituto != '* TRIAL * TRIA'
and instituto != '* TRIAL * TRIAL * TRIAL * TR'
and data_referencia  != 'N/A' 
and data_referencia != '* ' 
and data_referencia != '* T'
and data_referencia != '* TR'
and data_referencia != '* TRI'
and data_referencia != '* TRIA'
and data_referencia != '* TRIAL'
and data_referencia != '* TRIAL '
and data_referencia != '* TRIAL *'
and data_referencia != '* TRIAL * '
and data_referencia != '* TRIAL * T'
and data_referencia != '* TRIAL * TR'
and data_referencia != '* TRIAL * TRIAL '
and data_referencia != '* TRIAL * TRIA'
and data_referencia != '* TRIAL * TRIAL * TRIAL * TR'
and data_referencia != '* TRIAL * TRI'
and data_referencia != '* TRIAL * TRIAL *'
order by trial_turno_16


