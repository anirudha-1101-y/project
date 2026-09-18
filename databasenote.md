

## ==>mysql> select version();

+-----------+

| version() |

+-----------+

| 8.0.46    |

+-----------+

1 row in set (0.00 sec)

### 

### \--> mysql> select now();

+---------------------+

| now()               |

+---------------------+

| 2026-08-06 10:19:59 |

+---------------------+

1 row in set (0.01 sec)



### \--> mysql> select curtime();

+-----------+

| curtime() |

+-----------+

| 10:20:53  |

+-----------+

1 row in set (0.01 sec)



### \-->mysql> select curdate();

+------------+

| curdate()  |

+------------+

| 2026-08-06 |

+------------+

1 row in set (0.00 sec)



### \-->mysql> select user();

+----------------+

| user()         |

+----------------+

| root@localhost |

+----------------+

1 row in set (0.01 sec)



### \-->mysql> select database();

+------------+

| database() |

+------------+

| NULL       |

+------------+

1 row in set (0.00 sec)



mysql> select @@hostname;

+-----------------+

| @@hostname      |

+-----------------+

| DESKTOP-NJ3NT2B |

+-----------------+

1 row in set (0.00 sec)



mysql> @@port;

ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '@@port' at line 1

mysql> select @@port;

+--------+

| @@port |

+--------+

|   3306 |

+--------+

1 row in set (0.00 sec)



mysql> select 10+20;

+-------+

| 10+20 |

+-------+

|    30 |

+-------+

1 row in set (0.01 sec)



mysql> select 20%2;

+------+

| 20%2 |

+------+

|    0 |

+------+

1 row in set (0.00 sec)



mysql> select sqrt(144);

+-----------+

| sqrt(144) |

+-----------+

|        12 |

+-----------+

1 row in set (0.01 sec)



mysql> select SQRT(144);

+-----------+

| SQRT(144) |

+-----------+

|        12 |

+-----------+

1 row in set (0.00 sec)



mysql> select pow(2,5);

+----------+

| pow(2,5) |

+----------+

|       32 |

+----------+

1 row in set (0.01 sec)



mysql> select rand();

+--------------------+

| rand()             |

+--------------------+

| 0.5030967756203346 |

+--------------------+

1 row in set (0.01 sec)



mysql> select rand(1,2);

ERROR 1582 (42000): Incorrect parameter count in the call to native function 'rand'

mysql>

mysql>





==============================================

mysql> create database batch18;

Query OK, 1 row affected (0.09 sec)



mysql> show database;

ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'database' at line 1

mysql> show databases;

+--------------------+

| Database           |

+--------------------+

| batch18            |

| information\_schema |

| mysql              |

| performance\_schema |

| sys                |

+--------------------+

5 rows in set (0.08 sec)



mysql> create database if not exists batch18;

Query OK, 1 row affected, 1 warning (0.01 sec)



mysql> use batch18;

Database changed

mysql> select database();

+------------+

| database() |

+------------+

| batch18    |

+------------+

1 row in set (0.00 sec)



mysql> select database();

+------------+

| database() |

+------------+

| batch18    |

+------------+

1 row in set (0.00 sec)



mysql> create table student(id int,name varchar(20),age int);

Query OK, 0 rows affected (0.04 sec)



mysql> desc student;

+-------+-------------+------+-----+---------+-------+

| Field | Type        | Null | Key | Default | Extra |

+-------+-------------+------+-----+---------+-------+

| id    | int         | YES  |     | NULL    |       |

| name  | varchar(20) | YES  |     | NULL    |       |

| age   | int         | YES  |     | NULL    |       |

+-------+-------------+------+-----+---------+-------+

3 rows in set (0.02 sec)



mysql> show tables;

+-------------------+

| Tables\_in\_batch18 |

+-------------------+

| student           |

+-------------------+

1 row in set (0.01 sec)



mysql> create table teacher(name varchar(20));

Query OK, 0 rows affected (0.03 sec)



mysql> desc teacher;

+-------+-------------+------+-----+---------+-------+

| Field | Type        | Null | Key | Default | Extra |

+-------+-------------+------+-----+---------+-------+

| name  | varchar(20) | YES  |     | NULL    |       |

+-------+-------------+------+-----+---------+-------+

1 row in set (0.01 sec)



mysql> show tables;

+-------------------+

| Tables\_in\_batch18 |

+-------------------+

| student           |

| teacher           |

+-------------------+

2 rows in set (0.00 sec)



mysql> select \* from student;

Empty set (0.01 sec)



mysql> create table student1(id int primary key,name varchar(20),age int);

Query OK, 0 rows affected (0.02 sec)



mysql> desc student1;

+-------+-------------+------+-----+---------+-------+

| Field | Type        | Null | Key | Default | Extra |

+-------+-------------+------+-----+---------+-------+

| id    | int         | NO   | PRI | NULL    |       |

| name  | varchar(20) | YES  |     | NULL    |       |

| age   | int         | YES  |     | NULL    |       |

+-------+-------------+------+-----+---------+-------+

3 rows in set (0.00 sec)



mysql> create table employee as select \* from student1;

Query OK, 0 rows affected (0.03 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc employee;

+-------+-------------+------+-----+---------+-------+

| Field | Type        | Null | Key | Default | Extra |

+-------+-------------+------+-----+---------+-------+

| id    | int         | NO   |     | NULL    |       |

| name  | varchar(20) | YES  |     | NULL    |       |

| age   | int         | YES  |     | NULL    |       |

+-------+-------------+------+-----+---------+-------+

3 rows in set (0.01 sec)



mysql> create table emp1 as select id,name from student1;

Query OK, 0 rows affected (0.03 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc emp1;

+-------+-------------+------+-----+---------+-------+

| Field | Type        | Null | Key | Default | Extra |

+-------+-------------+------+-----+---------+-------+

| id    | int         | NO   |     | NULL    |       |

| name  | varchar(20) | YES  |     | NULL    |       |

+-------+-------------+------+-----+---------+-------+

2 rows in set (0.00 sec)



mysql> create table emp3 as select \* from student where 1!=2;

Query OK, 0 rows affected (0.03 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> insert into student values(101,"anirudha",30);

Query OK, 1 row affected (0.01 sec)



mysql> select \* from student;

+------+----------+------+

| id   | name     | age  |

+------+----------+------+

|  101 | anirudha |   30 |

+------+----------+------+

1 row in set (0.00 sec)



mysql> create table t1 select \* from student;

Query OK, 1 row affected (0.03 sec)

Records: 1  Duplicates: 0  Warnings: 0



mysql> select \* from t1;

+------+----------+------+

| id   | name     | age  |

+------+----------+------+

|  101 | anirudha |   30 |

+------+----------+------+

1 row in set (0.00 sec)







mysql> create table t2 select \* from student where 1=2;

Query OK, 0 rows affected (0.03 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> select \* from t2;

Empty set (0.00 sec)



mysql> desc t2;

+-------+-------------+------+-----+---------+-------+

| Field | Type        | Null | Key | Default | Extra |

+-------+-------------+------+-----+---------+-------+

| id    | int         | YES  |     | NULL    |       |

| name  | varchar(20) | YES  |     | NULL    |       |

| age   | int         | YES  |     | NULL    |       |

+-------+-------------+------+-----+---------+-------+

3 rows in set (0.00 sec)



mysql> desc t1;

+-------+-------------+------+-----+---------+-------+

| Field | Type        | Null | Key | Default | Extra |

+-------+-------------+------+-----+---------+-------+

| id    | int         | YES  |     | NULL    |       |

| name  | varchar(20) | YES  |     | NULL    |       |

| age   | int         | YES  |     | NULL    |       |

+-------+-------------+------+-----+---------+-------+

3 rows in set (0.00 sec)



mysql> select \* from t1;

+------+----------+------+

| id   | name     | age  |

+------+----------+------+

|  101 | anirudha |   30 |

+------+----------+------+

1 row in set (0.00 sec)



mysql> select \* from t2;

Empty set (0.00 sec)



mysql>

Note ::--> the create table .. as select {ctas} ::--> the create table as select  

&#x20;        is used to create a new table by coping data from  an exiting table or the result of the select query. It creates a new table automatically based on the column return by the select statement. It copy selected data ,column names, column data types, and column order. 

\--> Limitation of ctas is that it doesnot copy the table structure rule or database object . The following things are not copi3ed

1\. primary key

2\. foriegn key 

3\. Auto increment property 

4\. constaints

=================

\## INSERT command

case 1:

insert into tablename values(value1,value2,value3)







mysql> show databases;

+--------------------+

| Database           |

+--------------------+

| aniii              |

| batch18            |

| information\_schema |

| mysql              |

| performance\_schema |

| sys                |

+--------------------+

6 rows in set (0.04 sec)



mysql> use database batch18;

ERROR 1049 (42000): Unknown database 'database'

mysql> use batch18;

Database changed

mysql> creat table pystudent(id int,name varchar(20),age int,city varchar(30));

ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'creat table pystudent(id int,name varchar(20),age int,city varchar(30))' at line 1

mysql>  create table pystudent(id int,name varchar(20),age int,city varchar(30));

Query OK, 0 rows affected (0.08 sec)



mysql> insert into pysutdent values(101,"ani",30,"indore");

ERROR 1146 (42S02): Table 'batch18.pysutdent' doesn't exist

mysql> insert into pystudent values(101,"ani",30,"indore");

Query OK, 1 row affected (0.01 sec)



mysql> select \* from pystudent;

+------+------+------+--------+

| id   | name | age  | city   |

+------+------+------+--------+

|  101 | ani  |   30 | indore |

+------+------+------+--------+

1 row in set (0.01 sec)



mysql> insert into pystudent (id,name,city) values(102,"dev","rajwada");

Query OK, 1 row affected (0.01 sec)



mysql> select \* from pystudent;

+------+------+------+---------+

| id   | name | age  | city    |

+------+------+------+---------+

|  101 | ani  |   30 | indore  |

|  102 | dev  | NULL | rajwada |

+------+------+------+---------+

2 rows in set (0.00 sec)



mysql> insert into pystudent (name,id,city) values("dhruv",103,"dewas");

Query OK, 1 row affected (0.01 sec)



mysql> select \* from pystudent;

+------+-------+------+---------+

| id   | name  | age  | city    |

+------+-------+------+---------+

|  101 | ani   |   30 | indore  |

|  102 | dev   | NULL | rajwada |

|  103 | dhruv | NULL | dewas   |

+------+-------+------+---------+

3 rows in set (0.00 sec)



mysql> insert into pystudent set id=104, name="kuldeep",age=30,city="nepal";

Query OK, 1 row affected (0.01 sec)



mysql> select \* from pystudent;

+------+---------+------+---------+

| id   | name    | age  | city    |

+------+---------+------+---------+

|  101 | ani     |   30 | indore  |

|  102 | dev     | NULL | rajwada |

|  103 | dhruv   | NULL | dewas   |

|  104 | kuldeep |   30 | nepal   |

+------+---------+------+---------+

4 rows in set (0.00 sec)



mysql> insert into pystudent (id,name,age,city) values(105,"thapa",32,"indore"),(106,"saurabh",35,"betul");

Query OK, 2 rows affected (0.01 sec)

Records: 2  Duplicates: 0  Warnings: 0



mysql> select \* from pystudent;

+------+---------+------+---------+

| id   | name    | age  | city    |

+------+---------+------+---------+

|  101 | ani     |   30 | indore  |

|  102 | dev     | NULL | rajwada |

|  103 | dhruv   | NULL | dewas   |

|  104 | kuldeep |   30 | nepal   |

|  105 | thapa   |   32 | indore  |

|  106 | saurabh |   35 | betul   |

+------+---------+------+---------+

6 rows in set (0.00 sec)



mysql> create pybackup as select \* from pystudent where 1=0;

ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'pybackup as select \* from pystudent where 1=0' at line 1

mysql> create table pybackup as select \* from pystudent where 1=0;

Query OK, 0 rows affected (0.05 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> insert into pybackup select \*  from pystudent;

Query OK, 6 rows affected (0.01 sec)

Records: 6  Duplicates: 0  Warnings: 0



mysql> select \*from pystudent;

+------+---------+------+---------+

| id   | name    | age  | city    |

+------+---------+------+---------+

|  101 | ani     |   30 | indore  |

|  102 | dev     | NULL | rajwada |

|  103 | dhruv   | NULL | dewas   |

|  104 | kuldeep |   30 | nepal   |

|  105 | thapa   |   32 | indore  |

|  106 | saurabh |   35 | betul   |

+------+---------+------+---------+

6 rows in set (0.00 sec)



mysql> select \*from pybackup;

+------+---------+------+---------+

| id   | name    | age  | city    |

+------+---------+------+---------+

|  101 | ani     |   30 | indore  |

|  102 | dev     | NULL | rajwada |

|  103 | dhruv   | NULL | dewas   |

|  104 | kuldeep |   30 | nepal   |

|  105 | thapa   |   32 | indore  |

|  106 | saurabh |   35 | betul   |

+------+---------+------+---------+

6 rows in set (0.00 sec)



mysql> insert into pybackup(id,name) select id,name from pystudent;

Query OK, 6 rows affected (0.03 sec)

Records: 6  Duplicates: 0  Warnings: 0



mysql> select \* from pybackup;

+------+---------+------+---------+

| id   | name    | age  | city    |

+------+---------+------+---------+

|  101 | ani     |   30 | indore  |

|  102 | dev     | NULL | rajwada |

|  103 | dhruv   | NULL | dewas   |

|  104 | kuldeep |   30 | nepal   |

|  105 | thapa   |   32 | indore  |

|  106 | saurabh |   35 | betul   |

|  101 | ani     | NULL | NULL    |

|  102 | dev     | NULL | NULL    |

|  103 | dhruv   | NULL | NULL    |

|  104 | kuldeep | NULL | NULL    |

|  105 | thapa   | NULL | NULL    |

|  106 | saurabh | NULL | NULL    |

+------+---------+------+---------+



12 rows in set (0.00 sec)

&#x20;# concept of primary key



mysql> use batch18;

Database changed



way 1-->                  --------------------------

mysql> create table pyemployee(empid int primary key,name varchar(20),salary decimal(10,2));

Query OK, 0 rows affected (0.05 sec)



mysql> desc \* from pyemployeee;

ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '\* from pyemployeee' at line 1

mysql> desc pyemployee;

+--------+---------------+------+-----+---------+-------+

| Field  | Type          | Null | Key | Default | Extra |

+--------+---------------+------+-----+---------+-------+

| empid  | int           | NO   | PRI | NULL    |       |

| name   | varchar(20)   | YES  |     | NULL    |       |

| salary | decimal(10,2) | YES  |     | NULL    |       |

+--------+---------------+------+-----+---------+-------+

3 rows in set (0.03 sec)



way 2-->                      ------------------------------

mysql> create table employee2(empid int,name varchar(20),salary decimal(10,2),constraint pk\_employee primary key(empid));

Query OK, 0 rows affected (0.02 sec)



mysql> desc pyemployee2;

ERROR 1146 (42S02): Table 'batch18.pyemployee2' doesn't exist

mysql> desc employee2;

+--------+---------------+------+-----+---------+-------+

| Field  | Type          | Null | Key | Default | Extra |

+--------+---------------+------+-----+---------+-------+

| empid  | int           | NO   | PRI | NULL    |       |

| name   | varchar(20)   | YES  |     | NULL    |       |

| salary | decimal(10,2) | YES  |     | NULL    |       |

+--------+---------------+------+-----+---------+-------+

3 rows in set (0.00 sec)



way 3--> ------------------------------------------------

mysql> create table pyemployee3(empid int,name varchar(20),salary decimal(10,2));

Query OK, 0 rows affected (0.03 sec)



mysql> alter table pyemployee3 add primary key(empid);

Query OK, 0 rows affected (0.05 sec)

Records: 0  Duplicates: 0  Warnings: 0



mysql> desc pyemployee3;

+--------+---------------+------+-----+---------+-------+

| Field  | Type          | Null | Key | Default | Extra |

+--------+---------------+------+-----+---------+-------+

| empid  | int           | NO   | PRI | NULL    |       |

| name   | varchar(20)   | YES  |     | NULL    |       |

| salary | decimal(10,2) | YES  |     | NULL    |       |

+--------+---------------+------+-----+---------+-------+

3 rows in set (0.00 sec)



======================================================



mysql> select \* from pystudent;

+------+---------+------+---------+

| id   | name    | age  | city    |

+------+---------+------+---------+

|  101 | ani     |   30 | indore  |

|  102 | dev     | NULL | rajwada |

|  103 | dhruv   | NULL | dewas   |

|  104 | kuldeep |   30 | nepal   |

|  105 | thapa   |   32 | indore  |

|  106 | saurabh |   35 | betul   |

+------+---------+------+---------+

6 rows in set (0.01 sec)



mysql> desc pyemploee1;

ERROR 1146 (42S02): Table 'batch18.pyemploee1' doesn't exist

mysql> desc pyemployee1;

ERROR 1146 (42S02): Table 'batch18.pyemployee1' doesn't exist

mysql> desc pyemployee;

+--------+---------------+------+-----+---------+-------+

| Field  | Type          | Null | Key | Default | Extra |

+--------+---------------+------+-----+---------+-------+

| empid  | int           | NO   | PRI | NULL    |       |

| name   | varchar(20)   | YES  |     | NULL    |       |

| salary | decimal(10,2) | YES  |     | NULL    |       |

+--------+---------------+------+-----+---------+-------+

3 rows in set (0.01 sec)



mysql> insert into pyemployee values(101,"deepika",50000),(102,"rashmika",3000);

Query OK, 2 rows affected (0.02 sec)

Records: 2  Duplicates: 0  Warnings: 0



mysql> select \*from pyemployee;

+-------+----------+----------+

| empid | name     | salary   |

+-------+----------+----------+

|   101 | deepika  | 50000.00 |

|   102 | rashmika |  3000.00 |

+-------+----------+----------+

2 rows in set (0.01 sec)



mysql> insert into pyemployee(name,salary) values("thapaji",50000);



we not give any primary key values thatwhy they give error-->

ERROR 1364 (HY000): Field 'empid' doesn't have a default value

mysql>







mysql> insert into pyemployee(name,salary) values("thapaji",50000);

ERROR 1364 (HY000): Field 'empid' doesn't have a default value





question --1





mysql> create table product(pid int primary key,pname varchar(20),pcategory varchar(20),price int);

Query OK, 0 rows affected (0.04 sec)



mysql> desc product;

+-----------+-------------+------+-----+---------+-------+

| Field     | Type        | Null | Key | Default | Extra |

+-----------+-------------+------+-----+---------+-------+

| pid       | int         | NO   | PRI | NULL    |       |

| pname     | varchar(20) | YES  |     | NULL    |       |

| pcategory | varchar(20) | YES  |     | NULL    |       |

| price     | int         | YES  |     | NULL    |       |

+-----------+-------------+------+-----+---------+-------+

4 rows in set (0.01 sec)



mysql> insert into product(pid,pname,pcategory,price) values(101,laptop,electronic,50000),(102,smartphone

&#x20;   ->

&#x20;   -> insert into product(pid,pname,pcategory,price) values(101,laptop,electronic,50000),(102,smartphone^C

mysql> insert into product(pid,pname,pcategory,price) values(101,"laptop","electronic",50000),(102,"smartphone","electronic",5000),(103,"charger","electronic",250);

Query OK, 3 rows affected (0.01 sec)

Records: 3  Duplicates: 0  Warnings: 0



mysql> select \* from product;

+-----+------------+------------+-------+

| pid | pname      | pcategory  | price |

+-----+------------+------------+-------+

| 101 | laptop     | electronic | 50000 |

| 102 | smartphone | electronic |  5000 |

| 103 | charger    | electronic |   250 |

+-----+------------+------------+-------+

3 rows in set (0.00 sec)





\------------------------------------------------------------------------------------

\# concept of composite key -------







mysql> create table customer\_product(cid int,pid int,quntity int,primary key(cid,pid));

Query OK, 0 rows affected (0.04 sec)



mysql> desc customer\_product;

+---------+------+------+-----+---------+-------+

| Field   | Type | Null | Key | Default | Extra |

+---------+------+------+-----+---------+-------+

| cid     | int  | NO   | PRI | NULL    |       |

| pid     | int  | NO   | PRI | NULL    |       |

| quntity | int  | YES  |     | NULL    |       |

+---------+------+------+-----+---------+-------+

3 rows in set (0.01 sec)





mysql> insert into customer\_product values(101,5101,2);

Query OK, 1 row affected (0.01 sec)



mysql> insert into customer\_product values(102,5101,4);

Query OK, 1 row affected (0.01 sec)



mysql> select \* from customer\_product;

+-----+------+---------+

| cid | pid  | quntity |

+-----+------+---------+

| 101 | 5101 |       2 |

| 102 | 5101 |       4 |

+-----+------+---------+



mysql> insert into customer\_product values(102,5101,6);

ERROR 1062 (23000): Duplicate entry '102-5101' for key 'customer\_product.PRIMARY'





\----------------------------------------------------------------------------------------





mysql> create table students(stuid int,subid int,marks int,primary key(stuid,subid));

Query OK, 0 rows affected (0.04 sec)



mysql> desc students;

+-------+------+------+-----+---------+-------+

| Field | Type | Null | Key | Default | Extra |

+-------+------+------+-----+---------+-------+

| stuid | int  | NO   | PRI | NULL    |       |

| subid | int  | NO   | PRI | NULL    |       |

| marks | int  | YES  |     | NULL    |       |

+-------+------+------+-----+---------+-------+

\----------------------------------------------------------------------------------------



### \# auto increment -----------

mysql> create table pyemployee1(id int auto\_increment,name varchar(20),salary(10,2));

ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(10,2))' at line 1

mysql> create table pyemployee1(id int auto\_increment,name varchar(20),salary decimal(10,2));

ERROR 1075 (42000): Incorrect table definition; there can be only one auto column and it must be defined as a key

mysql> create table pyemployee1(id int auto\_increment primary key,name varchar(20),salary decimal(10,2));

Query OK, 0 rows affected (0.04 sec)



mysql> desc pyemployee1;

+--------+---------------+------+-----+---------+----------------+

| Field  | Type          | Null | Key | Default | Extra          |

+--------+---------------+------+-----+---------+----------------+

| id     | int           | NO   | PRI | NULL    | auto\_increment |

| name   | varchar(20)   | YES  |     | NULL    |                |

| salary | decimal(10,2) | YES  |     | NULL    |                |

+--------+---------------+------+-----+---------+----------------+

3 rows in set (0.00 sec)



mysql> insert into pyemployee1(name,salary) values("dhruv",5);

Query OK, 1 row affected (0.01 sec)



mysql> select \* from pyemployee1;

+----+-------+--------+

| id | name  | salary |

+----+-------+--------+

|  1 | dhruv |   5.00 |

+----+-------+--------+

1 row in set (0.00 sec)



mysql> insert into pyemployee1(name,salary) values("dhruv",5),("thatpa",45);

Query OK, 2 rows affected (0.01 sec)

Records: 2  Duplicates: 0  Warnings: 0



mysql> select \* from pyemployee1;

+----+--------+--------+

| id | name   | salary |

+----+--------+--------+

|  1 | dhruv  |   5.00 |

|  2 | dhruv  |   5.00 |

|  3 | thatpa |  45.00 |

+----+--------+--------+

3 rows in set (0.00 sec)



give error if we give direct value--



mysql> insert into pyemployee1 values("dhruv",522);

ERROR 1136 (21S01): Column count doesn't match value count at row 1

\----------------------------------------------------------------------------------------

mysql> create table pyemployee4(eid int auto\_increment  primary key,name varchar(20) )auto\_increment=100;

Query OK, 0 rows affected (0.04 sec)



mysql> desc pyemployee4;

+-------+-------------+------+-----+---------+----------------+

| Field | Type        | Null | Key | Default | Extra          |

+-------+-------------+------+-----+---------+----------------+

| eid   | int         | NO   | PRI | NULL    | auto\_increment |

| name  | varchar(20) | YES  |     | NULL    |                |

+-------+-------------+------+-----+---------+----------------+

2 rows in set (0.01 sec)



mysql> insert into pyemployee4 (name) values("dhruv"),("thapaji");

Query OK, 2 rows affected (0.01 sec)

Records: 2  Duplicates: 0  Warnings: 0



mysql> select \* from pyemployee4;

+-----+---------+

| eid | name    |

+-----+---------+

| 100 | dhruv   |

| 101 | thapaji |

+-----+---------+

2 rows in set (0.01 sec)

\---------------------------------------------------------------------------------------------------



### \# manually inserting auto\_increment value---



mysql> create table pyemployee5(eid int auto\_increment primary key,name varchar(20));

Query OK, 0 rows affected (0.03 sec)



mysql> insert into pyemployee5(name) values("thapaji");

Query OK, 1 row affected (0.01 sec)



mysql> select \* from pyemployee5;

+-----+---------+

| eid | name    |

+-----+---------+

|   1 | thapaji |

+-----+---------+

1 row in set (0.00 sec)



mysql> insert into pyemployee values(10,"kuldeep");

ERROR 1136 (21S01): Column count doesn't match value count at row 1

mysql> insert into pyemployee5 values(10,"kuldeep");

Query OK, 1 row affected (0.01 sec)



mysql> select \* from pyemployee5;

+-----+---------+

| eid | name    |

+-----+---------+

|   1 | thapaji |

|  10 | kuldeep |

+-----+---------+

2 rows in set (0.00 sec)



mysql> insert into pyemployee5(name) values("devendra");

Query OK, 1 row affected (0.01 sec)



mysql> select \* from pyemployee5;

+-----+----------+

| eid | name     |

+-----+----------+

|   1 | thapaji  |

|  10 | kuldeep  |

|  11 | devendra |

+-----+----------+

3 rows in set (0.00 sec)

\-----------------------------------------------------3





mysql> insert into pyemployee5 values(2,"kuldeep");

Query OK, 1 row affected (0.01 sec)



mysql> select \* from pyemployee5;

+-----+----------+

| eid | name     |

+-----+----------+

|   1 | thapaji  |

|   2 | kuldeep  |

|  10 | kuldeep  |

|  11 | devendra |

+-----+----------+

4 rows in set (0.00 sec)



mysql> insert into pyemployee5(name) values("saurabh");

Query OK, 1 row affected (0.01 sec)



mysql> select \* from pyemployee5;

+-----+----------+

| eid | name     |

+-----+----------+

|   1 | thapaji  |

|   2 | kuldeep  |

|  10 | kuldeep  |

|  11 | devendra |

|  12 | saurabh  |

+-----+----------+

5 rows in set (0.00 sec)

\------------------------------------------------------------------------------------------------

### \# auto increment with null value-





5 rows in set (0.00 sec)



mysql> create table pystudent1(sid int auto\_increment primary key,name varchar(20),age int);

Query OK, 0 rows affected (0.04 sec)                                                                                                    



mysql> insert into pystudent1(name,age) values("abc",30);

Query OK, 1 row affected (0.01 sec)



mysql> insert into pystudent1 values(null,"xyz",30);

Query OK, 1 row affected (0.01 sec)



mysql> select \* from pystudent1;

+-----+------+------+

| sid | name | age  |

+-----+------+------+

|   1 | abc  |   30 |

|   2 | xyz  |   30 |

+-----+------+------+



\----------------------------------------------------------------------------------------------

### \# auto increment with zero (0)--

mysql> insert into pystudent1 values(0,"xxx",30);

Query OK, 1 row affected (0.01 sec)



mysql> select \* from pystudent1;

+-----+------+------+

| sid | name | age  |

+-----+------+------+

|   1 | abc  |   30 |

|   2 | xyz  |   30 |

|   3 | xxx  |   30 |

+-----+------+------+

=----------------------------------------------------------------------------------------------



### \#find the mode--

mysql> select @@sql\_mode;

+-----------------------------------------------------------------------------------------------------------------------+

| @@sql\_mode                                                                                                            |

+-----------------------------------------------------------------------------------------------------------------------+

| ONLY\_FULL\_GROUP\_BY,STRICT\_TRANS\_TABLES,NO\_ZERO\_IN\_DATE,NO\_ZERO\_DATE,ERROR\_FOR\_DIVISION\_BY\_ZERO,NO\_ENGINE\_SUBSTITUTION |

+-----------------------------------------------------------------------------------------------------------------------+

1 row in set (0.01 sec)

\---------------------------------------------------------------------------------------------



