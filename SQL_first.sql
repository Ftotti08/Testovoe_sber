/*
CREATE table check_dates(
	date_id SERIAL PRIMARY KEY,
	check_date date
);

	
INSERT INTO check_dates(check_date)
VALUES(current_date);


do 
$$
begin
   for counter in 1..99 loop
		INSERT INTO check_dates(check_date)
		select date(max(check_date) + trunc(random()  * 6 + 2) * '1 day'::interval)
		FROM check_dates;
   end loop;
end; 
$$;
*/

SELECT *
FROM check_dates