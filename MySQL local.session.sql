create database if NOT EXISTS xyz;
use xyz;

create table employee(
id int primary key,
name varchar(50),
salary int
);

insert into  employee
(id, name, salary)
values
(1, "Adam", 25000),
(2, "bob", 30000),
(3, "Casey", 40000);

select * from employee;

insert into employee value (4, "Tom", 50000);
INSERT into employee VALUES (5, "Jerry", 60000);
INSERTinto employee values (6, "tim", 45000);