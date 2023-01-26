select
	ano,
	trial_cargo_5,
	trial_sigla_partido_22 
from microdados m 
where trial_nome_municipio_4 = 'Várzea Grande'

--Remover Repetições
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
