select 
	trial_instituto_8 as Instituto,
	ano as Ano_pesq,
	cargo as Cargo_Pretendido,
	sigla_uf is null as sigla,
	tipo as tipo_pesquisa,
	turno as Primeiro_Turno,
	trial_descricao_cenario_19  as cenario,
	nome_candidato as Candidato
from microdados m 
where trial_instituto_8 = 'Datafolha' 
and ano = 2022 
and cargo ='presidente' 
and tipo = 'estimulada'
and turno = 1 
and nome_candidato = 'Bolsonaro' or nome_candidato = 'Lula' or nome_candidato = 'Ciro' or nome_candidato = 'Simone Tebet'
and trial_descricao_cenario_19 = 'cenário 1 - estimulado - 1º turno'




select nome_candidato  from microdados m where trial_instituto_8 = 'Datafolha' and ano = 2022 and cargo = 'presidente'