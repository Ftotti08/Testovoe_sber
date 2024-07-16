/*
CREATE TABLE transfers(
	"from"  INT NOT NULL,
	"to" INT NOT NULL, 
	amount INT NOT NULL,
	tdate DATE
);


INSERT INTO transfers
SELECT trunc(random()  * 3 + 1),
		trunc(random()  * 3 + 1),
		trunc(random()  * 10 + 1)*100,
		current_date;

do 
$$
begin
   for counter in 1..5 loop
		INSERT INTO transfers("from", "to", amount, tdate)
		SELECT  trunc(random()  * 3 + 1),
				trunc(random()  * 3 + 1),
				trunc(random()  * 10 + 1)*100,
				date(max(tdate) + trunc(random()  * 6 + 2) * '1 day'::interval)
		FROM transfers;
				
   end loop;
end; 
$$;

*/

SELECT acc,
		tdate as dt_from,
		LEAD(tdate,1, DATE('01-01-3000')) OVER (PARTITION BY acc) as dt_to,
		SUM(amount) OVER (PARTITION BY acc ORDER BY tdate) as balance
FROM		
	(SELECT tdate,
		"from" as acc,
		- amount as amount
	FROM transfers
	UNION ALL
		SELECT tdate,
		"to" as acc,
		amount as amount
		FROM transfers
	ORDER BY acc, tdate) as t1


