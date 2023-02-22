USE pds;
#1
SELECT * FROM employees ORDER BY first_name;
#2
SELECT first_name, last_name, salary, salary * 0.15 AS tax FROM employees;
#3
SELECT SUM(salary) AS total_salary FROM employees;
#4
SELECT MAX(salary) AS max_salary, MIN(salary) AS min_salary FROM employees;
#5
SELECT AVG(salary) AS average_salary, COUNT(employee_id) AS total_employees FROM employees;