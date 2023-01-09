select 
	count(distinct t2.seller_id) as qtde_vendedores 
from tb_order t1 
left join tb_order_item as t2 
on t1.order_id = t2.order_id 
where t1.order_approved_at  between '2017-06-01' and '2018-06-01'