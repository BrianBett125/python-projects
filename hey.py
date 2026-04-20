     1	print('hello world January 2026')
     2	
     3	print("hello, python")
     This chapter provides you with the information you need to create your first database
     This chapter provides you with the information you need to create your first database
and to create the tables and associated data used for the examples in this book. You
will also learn about various data types and see how to create tables using them.
Because the examples in this book are executed against a MySQL database, this chap‐
ter is somewhat skewed toward MySQL’s features and syntax, but most concepts are
applicable to any server.
Creating a MySQL Database
If you want the ability to experiment with the data used for the examples in this book,
you have two options:
• Download and install the MySQL server version 8.0 (or later) and load the Sakila
example database from https://dev.mysql.com/doc/index-other.html.
• Go to https://www.katacoda.com/mysql-db-sandbox/scenarios/mysql-sandbox to
access the MySQL Sandbox, which has the Sakila sample database loaded in a
MySQL instance. You’ll have to set up a (free) Katacoda account. Then, click the
Start Scenario button.
If you choose the second option, once you start the scenario, a MySQL server is
installed and started, and then the Sakila schema and data are loaded. When it’s ready,
a standard mysql> prompt appears, and you can then start querying the sample data‐
base. This is certainly the easiest option, and I anticipate that most readers will
choose this option; if this sounds good to you, feel free to skip ahead to the next
section.
If you prefer to have your own copy of the data and want any changes you have made
to be permanent, or if you are just interested in installing the MySQL server on your
17
own machine, you may prefer the first option. You may also opt to use a MySQL
server hosted in an environment such as Amazon Web Services or Google Cloud. In
either case, you will need to perform the installation/configuration yourself, as it is
beyond the scope of this book. Once your database is available, you will need to fol‐
low a few steps to load the Sakila sample database.
First, you will need to launch the mysql command-line client and provide a password,
and then perform the following steps:
1. Go to https://dev.mysql.com/doc/index-other.html and download the files for
“sakila database” under the Example Databases section.
2. Put the files in a local directory such as C:\temp\sakila-db (used for the next two
steps, but overwrite with your directory path).
3. Type source c:\temp\sakila-db\sakila-schema.sql; and press Enter.
4. Type source c:\temp\sakila-db\sakila-data.sql; and press Enter.
You should now have a working database populated with all the data needed for the
examples in this book.
The Sakila sample database is made available by MySQL and is
licensed via the New BSD license. Sakila contains data for a ficti‐
tious movie rental company, and includes tables such as store,
inventory, film, customer, and payment. While actual movie rental
stores are largely a thing of the past, with a little imagination we
and to create the tables and associated data used for the examples in this book. You
will also learn about various data types and see how to create tables using them.
Because the examples in this book are executed against a MySQL database, this chap‐
ter is somewhat skewed toward MySQL’s features and syntax, but most concepts are
applicable to any server.
Creating a MySQL Database
If you want the ability to experiment with the data used for the examples in this book,
you have two options:
• Download and install the MySQL server version 8.0 (or later) and load the Sakila
example database from https://dev.mysql.com/doc/index-other.html.
• Go to https://www.katacoda.com/mysql-db-sandbox/scenarios/mysql-sandbox to
access the MySQL Sandbox, which has the Sakila sample database loaded in a
MySQL instance. You’ll have to set up a (free) Katacoda account. Then, click the
Start Scenario button.
If you choose the second option, once you start the scenario, a MySQL server is
installed and started, and then the Sakila schema and data are loaded. When it’s ready,
a standard mysql> prompt appears, and you can then start querying the sample data‐
base. This is certainly the easiest option, and I anticipate that most readers will
choose this option; if this sounds good to you, feel free to skip ahead to the next
section.
If you prefer to have your own copy of the data and want any changes you have made
to be permanent, or if you are just interested in installing the MySQL server on your
17
own machine, you may prefer the first option. You may also opt to use a MySQL
server hosted in an environment such as Amazon Web Services or Google Cloud. In
either case, you will need to perform the installation/configuration yourself, as it is
beyond the scope of this book. Once your database is available, you will need to fol‐
low a few steps to load the Sakila sample database.
First, you will need to launch the mysql command-line client and provide a password,
and then perform the following steps:
1. Go to https://dev.mysql.com/doc/index-other.html and download the files for
“sakila database” under the Example Databases section.
2. Put the files in a local directory such as C:\temp\sakila-db (used for the next two
steps, but overwrite with your directory path).
3. Type source c:\temp\sakila-db\sakila-schema.sql; and press Enter.
4. Type source c:\temp\sakila-db\sakila-data.sql; and press Enter.
You should now have a working database populated with all the data needed for the
examples in this book.
The Sakila sample database is made available by MySQL and is
licensed via the New BSD license. Sakila contains data for a ficti‐
tious movie rental company, and includes tables such as store,
inventory, film, customer, and payment. While actual movie rental
stores are largely a thing of the past, with a little imagination we
