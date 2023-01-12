#Mostrando a data minima e a máxima 
select 
	max(order_approved_at),
	min(order_approved_at) 
from tb_order
--------------------------------------------------------------------------------------------------

#Descobrindo a base ativa 
#Definimos que a base ativa é quem faz compras no ultimo ano 
#Podemos observar que nesse ano (2017-2018) temos um total de 2290 vendedores ativos
select 
	count(distinct t2.seller_id) as qtde_vendedores,
	max(order_approved_at),
	min(order_approved_at) 
from tb_order t1 
left join tb_order_item as t2 
on t1.order_id = t2.order_id 
where t1.order_approved_at  between '2017-06-01' and '2018-06-01'

-----------------------------------------------------------------------------------------------------

#Criando variáveis em relação a base ativa 
#Codigo abaixo refere quem são os vendedores mais produtivos (que vendem mais)

select 
	t2.seller_id,
	sum(t2.price) as receita_total,
	count(t1.order_id) as qtd_pedidos
from tb_order t1 
left join tb_order_item as t2 
on t1.order_id = t2.order_id 
where t1.order_approved_at  between '2017-06-01' and '2018-06-01'
group by t2.seller_id 

-------------------------------------------------------------------------------------------------------

#Codigo abaixo refere a quantidade de produtos e produtos distintos vendidos

select 
	t2.seller_id,
	sum(t2.price) as receita_total,
	count(distinct t1.order_id) as qtd_pedidos,
	count(t2.product_id) as qtd_produtos, 
	count( distinct t2.product_id) as qtd_produtos_distintos
from tb_order t1 
left join tb_order_item as t2 
on t1.order_id = t2.order_id 
where t1.order_approved_at  between '2017-06-01' and '2018-06-01'
group by t2.seller_id 

-------------------------------------------------------------------------------------------------------

#codigo abaixo mostra a quantidade em dias que o vendedor faz a ultima venda, (Não está completo)

select
	t2.seller_id,
	sum(t2.price) as receita_total,
	count(distinct t1.order_id) as qtd_pedidos,
	count(t2.product_id) as qtd_produtos, 
	count( distinct t2.product_id) as qtd_produtos_distintos,
	extract ()
	--age(convert(varchar(10) t1.order_approved_at, 103), '2018-06-01')	
	--to_char(t1.order_approved_at - '2018-06-01') as qtd_ult_vnda
	--min(date_part('day', interval '1 year')) as qtd_dias_ultima_venda
	--min(cast(julianday('2018-06-01') - julianday(t1.order_approved_at) as int)) as qtd_dias_ult_venda
from tb_order t1 
left join tb_order_item as t2 
on t1.order_id = t2.order_id 
where t1.order_approved_at  between '2017-06-01' and '2018-06-01'
group by t2.seller_id 

-----------------------------------------------------------------------------------------------------------
##Descobrindo a data da primeira venda de cada vendedor que está na minha base de dados

select
	t2.seller_id,
	min(t1.order_approved_at) 
from tb_order t1 
left join tb_order_item t2 
on t1.order_id = t2.order_id 
group by t2.seller_id 

--------------------------------------------------------------------------------------------------------------
--Juntando Todos as consultas acima ficamos com:



	select
		t2.seller_id,
		sum(t2.price) as receita_total,
		count(distinct t1.order_id) as qtd_pedidos,
		count(t2.product_id) as qtd_produtos, 
		count( distinct t2.product_id) as qtd_produtos_distintos,
		min(to_timestamp(t1.order_approved_at,'YYYYMMDD HH24:MI:SS')  - to_timestamp('2018-06-01 00:00:00','YYYYMMDD HH24:MI:SS')) as qtd_dias_ult_venda,
		max(to_timestamp('2018-06-01 00:00:00','YYYYMMDD HH24:MI:SS') - to_timestamp(t1.order_approved_at,'YYYYMMDD HH24:MI:SS'))
	from tb_order t1 
	left join tb_order_item as t2 
	on t1.order_id = t2.order_id
	left join (
		select
			t2.seller_id,
			min(to_timestamp(t1.order_approved_at,'YYYYMMDD HH24:MI:SS')) as data_inicio
		from tb_order t1 
		left join tb_order_item t2 
		on t1.order_id = t2.order_id 
		group by t2.seller_id 
	) as t3
	on t2.seller_id  = t3.seller_id
	where t1.order_approved_at  between '2017-06-01' and '2018-06-01'
	group by t2.seller_id 
	
	
	
	select * from tb_order to2 






