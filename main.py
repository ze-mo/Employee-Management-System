import employee_class
import hashlib

import mysql.connector
from prettytable import PrettyTable

#Initializes a connection to the database
print("Please connect to the Database of choice\n")
while True:
    usr = input("Username: ")
    password = input("Password: ")
    hostname = input("Hostname: ")
    db_name = input("\nDatabase name: ")

    try:
        db = mysql.connector.connect(
            host=hostname,
            user=usr,
            passwd=password,
            database=db_name
            )
        break
    except Exception:
        print("Invalid credentials!\n")

#Sets a cursor to execute queries
mycursor = db.cursor()

salt = 'salt123'

def check_department(dep_name):
    mycursor.execute("SELECT dep_name FROM department")
    departments = [x[0] for x in mycursor]
    if dep_name not in departments:
        raise ValueError("Department not in list of departments: IT, Sales, Corporate")

def login(): 
    """Takes in a username and password as input, hashes the password and checks the database 
    for a combination of the username and hash."""

    global username
    global check_usr
    check_usr = ()
    while not check_usr:
        username, password = input("Username: "), input("Password: ")
        dk = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf8'), bytes(salt, 'utf8'), 10000)
        mycursor.execute(f"SELECT username FROM login_info WHERE username = '{username}' AND password = '{dk.hex()}'")
        for value in mycursor:
            check_usr += value
        if check_usr:
            break
        else:
            print("\nInvalid credentials!")
            continue

def register():
    """Takes in a username and password as input, appends them to a login table in the DB 
    and adds a row in the employee table based on input. 
    The stored passwords are hashed."""

    username, password = input('Username: '), input('Password: ')
    dk = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf8'), bytes(salt, 'utf8'), 10000)
    mycursor.execute("SELECT username FROM login_info")
    l_users = [x[0] for x in mycursor]
    if username in l_users:
        print("\nThat user already exists!")     
    else:
        mycursor.execute(f"INSERT INTO login_info (username, password) VALUES ('{username}', '{dk.hex()}')")
        db.commit()
        add_employee()
        print("\nYou have successfully registered!")

def check_admin(username):
    return bool(username == 'admin')

def assign_project():
    employee_id = input("Choose an employee by ID: ")
    mycursor.execute(f"SELECT dep_id FROM employee_main_info WHERE emp_id = {int(employee_id)}")
    department_id = 0
    for x in mycursor:
        department_id += int("".join(str(t) for t in x))
    mycursor.execute(f"SELECT project_id FROM works_on WHERE dep_id = {department_id}")
    projects_id = [y[0] for y in mycursor]

    while True:
        try:
            mode = input(f"Available projects for department '{department_id}' are: {projects_id}. Choose project_id: ")
            mycursor.execute(f"UPDATE employee_main_info SET project_id = {int(mode)} WHERE emp_id = {int(employee_id)}")
            db.commit()
            print("\nYou've assigned project successfully!")

            query_describe_table = ['emp_id', 'first_name', 'last_name', 'dep_id', 'project_id']
            query_view_table = (f"SELECT emp_id, first_name, last_name, dep_id, project_id FROM employee_main_info WHERE emp_id = {employee_id}")
            open_table(query_describe_table, query_view_table)
            break
        except Exception:
            print("\nYou didn't choose a project correctly!")
            continue

def change_salary():
    employee_id = input("Choose an employee by ID: ")
    mycursor.execute(f"SELECT salary FROM employee_main_info WHERE emp_id = {int(employee_id)}")
    salary = [x[0] for x in mycursor]
    if salary != [None]:
        salary = int("".join(str(t) for t in salary))
    else:
        salary = 0

    while True:
        try:
            mode = input(f"Current employee salary is {salary}. Choose a new value: ")
            mycursor.execute(f"UPDATE employee_main_info SET salary = {int(mode)} WHERE emp_id = {int(employee_id)}")
            db.commit()
            print("\nYou've changed the salary successfully!")
            query_describe_table = ['emp_id', 'first_name', 'last_name', 'salary']
            query_view_table = (f"SELECT emp_id, first_name, last_name, salary FROM employee_main_info WHERE emp_id = {employee_id}")
            open_table(query_describe_table, query_view_table)
            break

        except Exception:
            print("\nYou entered an invalid value!")
            break

def open_table(field_query, rows_query):
    if type(field_query) != list:
        mycursor.execute(field_query)
        fields = [x[0] for x in mycursor]
        table_view = PrettyTable(fields)
    else:
        table_view = PrettyTable(field_query)
    mycursor.execute(rows_query)
    table_view.add_rows(mycursor)
    print(table_view)

def set_dep_id(dep_name, location):
    dep_info = []
    query_extract_dep = f"SELECT dep_id FROM department WHERE dep_name = '{dep_name}' AND location = '{location}'"
    mycursor.execute(query_extract_dep)
    for x in mycursor:
        dep_info.append(x)

    for dep in dep_info:
        mycursor.execute(f"UPDATE employee_main_info SET dep_id = {dep[0]} WHERE emp_id = LAST_INSERT_ID()")
        db.commit()

def view_table_employee(): 
    if check_admin(username): #Full employee table with visible sensitive info (admin permission required)
        query_describe_table = ("DESC employee_main_info")
        query_view_table = ("SELECT emp_id, first_name, last_name, DATE_FORMAT(birth_day,'%d/%m/%Y'), sex, cast(aes_decrypt(social_security_number, 'key1234') as char(100)), salary, dep_id, project_id, location FROM employee_main_info")
    else: #Limited table for employees with no admin priviliges
        query_describe_table = ['emp_id', 'first_name', 'last_name', 'birth_day', 'sex', 'dep_id', 'project_id', 'location']
        query_view_table = ("SELECT emp_id, first_name, last_name, DATE_FORMAT(birth_day,'%d/%m/%Y'), sex, dep_id, project_id, location FROM employee_main_info")
    open_table(query_describe_table, query_view_table)

def view_table(table):
    query_describe_table = (f"DESC {table}")
    query_view_table = (f"SELECT * FROM {table}")
    open_table(query_describe_table, query_view_table)

def add_employee():
    print("\nPlease enter employee data: ")
    while True:
        try:
            new_emp = employee_class.Employee.from_input()
            info_list = [
            new_emp.first_name, 
            new_emp.last_name, 
            new_emp.birth_day, 
            new_emp.sex, 
            new_emp.social_security_number,
            new_emp.location
            ]
            dep_name = input("Department: ")

            if new_emp.sex != 'M' and new_emp.sex != 'F':
                raise ValueError("Gender options are M/F")
            if new_emp.location != 'Sofia' and new_emp.location != 'Plovdiv':
                raise ValueError("Chosen location must be Sofia or Plovdiv")
            if len(new_emp.social_security_number) != 10:
                raise ValueError("SSN should be 10 digits long")

            check_department(dep_name)
            query_main_info = ("INSERT INTO employee_main_info (first_name, last_name, birth_day, sex, social_security_number, location) VALUES (%s, %s, %s, %s, aes_encrypt(%s, 'key1234'), %s)")
            mycursor.execute(query_main_info, info_list) #Sensitive info is encrypted before it's stored in the database
            set_dep_id(dep_name, new_emp.location)
            break

        except Exception as e:
            print(e)
            print("\nPlease enter data correctly!")
    db.commit()

def view_mode(): #View option after login stage
    tables_list = ['employee', 'project', 'department', 'works_on', 'client']
    table = input(f"\nView table {tables_list}: ").lower()
    if table == 'employee':
        perform_operation_decorator(table)
    else:
        perform_operation_decorator(table, table)

def modify_mode(): #Modify option after login stage
    if check_admin(username):
        mode = input("Assign a project to an employee or change their salary? (assign/change): ").lower()
        perform_operation_decorator(mode)
    else:
        print("\nYou don't have permission to do that!")

def perform_operation_decorator(chosen_operation, *args):
    """Function containing a dictionary with all the necessary input values 
    and their corresponding functions. When executed with the input as a parameter, 
    it calls a function taking as many arguments, as needed."""

    operations = {
        'employee': view_table_employee,
        'project': view_table,
        'department': view_table,
        'works_on': view_table,
        'client': view_table,
        'assign': assign_project,
        'change': change_salary,
        'login': login,
        'register': register,
        'view': view_mode,
        'modify': modify_mode
    }

    chosen_operation_function = operations.get(chosen_operation, "Invalid Input")
    try:
        return chosen_operation_function(*args)
    except Exception:
        print("Invalid Input")

def main():
    print("Welcome to the company database!")
    while True:
        mode = input("\nLogin or Register? (q to quit): ").lower()
        if mode == 'login':
            perform_operation_decorator(mode)
            while check_usr:   #if login mode was selected, checks if user exists and goes into the loop, otherwise it will skip.
                mode = input("\nWould you like to view or modify information? (view/modify/q to quit): ").lower()
                if mode == 'q':
                    break
                else:
                    perform_operation_decorator(mode)

        elif mode == 'register':
            perform_operation_decorator(mode)

        elif mode == 'q':
            break

        else:
            print("Invalid Input")

        mode = input("\nWould you like to continue? (y/n): ").lower()
        if mode == 'n':
            break                                                      

if __name__ == '__main__':
    main()

print("\nHave a nice day!")