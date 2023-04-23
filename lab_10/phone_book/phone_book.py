import psycopg2
from config import host, user, password, db_name
connection = None


data_from_console = None
cursor = None
try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True


    # CREATE A TABLE
    with connection.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE phone_book (
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(150) NOT NULL,
            phone_num VARCHAR(15) NOT NULL
            )
            """
        )
        print("[INFO] Table created successfully!")



    # INSERTING DATA TO TABLE FROM CSV FILE
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """
    #         COPY phone_book (user_name, phone_num)
    #         FROM 'C:/Users/qasob/OneDrive/Documents/GitHub/PP2_lab_GhQ/lab_10/phone_book/csv/csv_for_lab10_phone_book.csv'
    #         DELIMITER ','
    #         CSV HEADER;
    #         """
    #     )
    #
    #     print("[INFO] Inserted successfully!")





    # cursor = connection.cursor()





    # INSERTING DATA FROM CONSOLE
    # N = int(input("Enter number of Users: "))
    # print("Enter USER NAME and his PHONE NUMBER separated by SPACE:")
    # for i in range(N):
    #     data = input()
    #     cursor.execute(
    #         """
    #         INSERT INTO public.phone_book(user_name, phone_num)
    #         VALUES (%s, %s);
    #         """, (data.split())
    #     )



    # UPDATING PHONE NUMBER BY NAME
    # user_name = input("Enter user first name: ")
    # phone_num_update = input("Enter new phone number: ")
    # cursor.execute("""
    #     UPDATE phone_book
    #     SET phone_num = (%s)
    #     WHERE
    #     user_name = (%s)
    #     """, (phone_num_update, user_name))



    # UPDATING NAME BY PHONE NUMBER
    # phone_num_update = input("Enter phone number: ")
    # user_name = input("Enter user's new name: ")
    # cursor.execute("""
    #         UPDATE phone_book
    #         SET user_name = (%s)
    #         WHERE
    #         phone_num = (%s)
    #         """, (user_name, phone_num_update))


    # UPDATE NAME
    # crrnt_name = input("Enter current name: ")
    # updated_name = input("Enter new name: ")
    # cursor.execute("""
    #         UPDATE phone_book
    #         SET user_name = (%s)
    #         WHERE
    #         user_name = (%s)
    #         """, (updated_name, crrnt_name))


    # UPDATING PHONE NUMBER
    # crrnt_phone_num = input("Enter current phone number: ")
    # updated_phone_num = input("Enter new phone number: ")
    # cursor.execute("""
    #         UPDATE phone_book
    #         SET phone_num = (%s)
    #         WHERE
    #         phone_num = (%s)
    #         """, (updated_phone_num, crrnt_phone_num))


    # MAIN: UPDATING ROW DATA
    # user_id = int(input('Enter user id: '))
    # updated_user_name = input('Enter new user name: ')
    # updated_phone_num = input('Enter new phone number: ')
    # cursor.execute("""
    #         UPDATE phone_book
    #         SET user_name = (%s), phone_num = (%s)
    #         WHERE
    #         user_id = (%s)
    #         """, (updated_user_name ,updated_phone_num, user_id))




    # QUERYING THROUGH THE PHONE BOOK
    # fetches users with phone numbers containing 54
    # cursor.execute(
    #     """
    #     SELECT user_id, user_name from phone_book WHERE phone_num like '%54%'
    #     """
    # )
    #
    # print("Number of users:", cursor.rowcount)
    # row = cursor.fetchone()
    # while row is not None:
    #     print(row)
    #     row = cursor.fetchone()



    # fetches users with id less than N
    # cursor.execute(
    #     """
    #     SELECT user_name, phone_num from phone_book WHERE user_id <= 3
    #     """
    # )
    # rows = cursor.fetchall()
    #
    # for row in rows:
    #     print(row)




    # DELETING DATA BY NAME
    # user_name = input('Enter user name: ')
    # cursor.execute(
    #     """
    #     DELETE FROM phone_book
    #     WHERE user_name = 'Titus'
    #     """)



except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:

        connection.close()
        print("[INFO] PostgreSQL closed successfully!")