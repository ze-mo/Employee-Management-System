# Employee-Management-System

Project about a Database-driven Employee Management System. The repository consists of a MySQL database, an employee management Python script allowing reading and modifying information in the DB, SQL file for initializing the database, employee class module and a requirements file.

The cycle of the program is a login & register menu, which lead to the appropriate functionality. 
Such functionality includes features as:
- viewing tables
- adding employees to the database
- assigning projects
- changing salary
etc.

The idea is that we perform different changes in our Employee Record by using different functions inside of our script.


Setup instructions
-------------------
This project presumes you have Python 3 installed.

Download MySQL:
1. Open up a browser and go to: http://dev.mysql.com/downloads/mysql/
2. Scroll to the list of available downloads. Click the 'Download' button next to the applicable download.
3. Follow the configuration steps 
4. On the Security Options screen, specify a new root password
5. After all the Configuration steps have run, you have successfully installed MySQL.

Customizing the PATH for MySQL Tools:
1. Copy the path of your MySQL Server/bin directory & add it as a new environment variable in the Path variable.
https://dev.mysql.com/doc/mysql-windows-excerpt/5.7/en/mysql-installation-windows-path.html

Create a local copy of the repository:
1. Open Git Bash terminal
2. Move to a directory where you wish to store your repo
3. Run: git clone https://github.com/ze-mo/Employee-Management-System.git

Getting the requirements:
1. Open a terminal of your choice (run as administrator)
2. Go to the directory in which you store your copy of the repository
3. Activate your virtual environment
4. Run: pip install -r requirements.txt 

Creating the database:
1. Run the db_deployment.py script to create an empty database
2. Import the seed.sql file into the new database
> mysql -u root -p 'database_name' < seed.sql

Running the program:
1. Run the main.py script
------------------
