import mysql.connector

def create_db():
    print('Enter credentials to make a MySQL connection: ')
    while True:
        db = ''
        usr = input("Username: ")
        password = input("Password: ")
        hostname = input("Hostname: ")

        try:
            db = mysql.connector.connect(
                host=hostname,
                user=usr,
                passwd=password
                )
            break
        except Exception:
            print("Invalid credentials!\n")


    db_name = input("\nChoose Database name: ")
    mycursor = db.cursor()
    mycursor.execute(f"CREATE DATABASE {db_name}")
    print(f"\nDatabase {db_name} created successfully!")

create_db()

