# Employee-Management-System

Project about a Database-driven Employee Management System. The repository consists of a MySQL database, an employee management Python script allowing reading and modifying information in the DB, SQL file for initializing the database, employee class module and a requirements file.

The cycle of the program is a login & register menu, which lead to the appropriate functionality. 
Such functionality includes features as:
- adding employees to the database
- assigning projects
- changing salary
etc.

The idea is that we perform different changes in our Employee Record by using different functions inside of our script.


Setup instructions
-------------------

Create a new database:
- open MySQL shell
- \sql (switches to SQL processing mode)
- \connect <username>@<hostname>
- CREATE DATABASE company_db_simulation;

Copy the seed.sql file to your MySQL Server/bin folder

Import the seed.sql file into the new database from cmd (run as administrator):
- mysql -u root -p company_db_simulation < seed.sql (this command needs to be ran in your MySQL Server/bin folder)

Additionally, you need to set your hostname, username and password of your connection in the employee_management.py script.
---------

Now, you are ready to run the program.
Enjoy!
