/*
CREATE TABLE employee(
	id SERIAL PRIMARY KEY,
	name varchar(40)
);


CREATE TABLE sales(
	id SERIAL PRIMARY KEY,
	employee_id INT NOT NULL,
	FOREIGN KEY(employee_id) REFERENCES employee(id),
	price INT
);


INSERT INTO employee(name)
VALUES('John'), ('Alex'), ('Michael'), ('Peter'), ('Jimm'), ('Will')



do 
$$
begin
   for counter in 1..100 loop
		INSERT INTO sales(employee_id, price)
		SELECT trunc(random()  * 6 + 1), trunc(random()  * 1000 + 1);
   end loop;
end; 
$$;
*/

SELECT employee.id,
	name,
	Count(price) as sales_c, 
	SUM(price) as sales_s,
	RANK() OVER (ORDER BY Count(price) DESC) AS sales_rank_c,
	RANK() OVER (ORDER BY SUM(price) DESC) AS sales_rank_s
FROM sales JOIN employee ON employee.id = sales.employee_id
GROUP BY employee.id