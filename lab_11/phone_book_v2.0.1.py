import psycopg2
from config import host, user, password, db_name
connection = None
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
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """
    #         CREATE TABLE phone_book (
    #         user_id SERIAL PRIMARY KEY,
    #         user_name VARCHAR(150) NOT NULL,
    #         user_surname VARCHAR(150) NOT NULL,
    #         phone_num VARCHAR(15) NOT NULL
    #         )
    #         """
    #     )
    #     print("[INFO] Table created successfully!")


    # cursor = connection.cursor()



    # Function that returns all records based on a pattern

    # CREATE OR REPLACE FUNCTION return_records(pattern VARCHAR) -- used this one
    # RETURNS SETOF phone_book AS $$
    # BEGIN
    #   RETURN QUERY SELECT * FROM phone_book WHERE user_name LIKE '%' || pattern || '%' or user_surname LIKE '%' || pattern || '%' or phone_num LIKE '%' || pattern || '%';
    # END;
    # $$ LANGUAGE plpgsql;



    # procedure to insert new user by name and phone, update phone if user already exists

    # data = input("FIRST name, LAST name, phone NUMBER (separated by space): ").split()
    # cursor.execute(
    #     """
    #     SELECT user_name
    #     FROM phone_book
    #     WHERE user_name = %s or user_surname = %s
    #     """, (data[0], data[1])
    # )
    # res = cursor.fetchone()
    #
    # if res is not None:
    #     cursor.execute(
    #         """
    #         UPDATE phone_book
    #         SET phone_num = %s
    #         WHERE user_name = %s or user_surname = %s
    #         """, (data[2], data[0], data[1])
    #     )
    #
    # else:
    #     cursor.execute(
    #         """
    #         INSERT INTO phone_book(user_name, user_surname, phone_num)
    #         VALUES (%s, %s, %s)
    #         """, data
    #     )




    #  function to querying data from the tables with pagination (by limit and offset)

    # CREATE OR REPLACE FUNCTION get_data(lim INTEGER, off_set INTEGER, num VARCHAR)
    # RETURNS SETOF phone_book AS $$
    # BEGIN
    #   RETURN QUERY SELECT * FROM phone_book WHERE phone_num LIKE num LIMIT lim OFFSET off_set;
    # END;
    # $$ LANGUAGE plpgsql;



    # procedure to deleting data from tables by username or phone

    # DELETING DATA BY NAME
    # user_name = input('Enter user name/surname: ')
    # cursor.execute(
    #     """
    #     DELETE FROM phone_book
    #     WHERE user_name = %s OR user_surname = %s
    #     """, (user_name, user_name))


    # DELETING DATA BY PHONE NUMBER
    # user_phone_num = input('Enter user phone num: ')
    # cursor.execute(
    #     """
    #     DELETE FROM phone_book
    #     WHERE phone_num = %s
    #     """, (user_phone_num, ))

# -- CREATE
# OR
# REPLACE
# PROCEDURE
# insert_user(
#     --    IN
# usr_name
# VARCHAR(30),
# --    IN
# usr_surname
# VARCHAR(30),
# --    IN
# usr_phone_num
# VARCHAR(30)
# - - )
# -- LANGUAGE
# 'plpgsql'
#
# -- AS
# -- $$
#
# -- DECLARE
# --    DECLARE
# usr_id
# INT;
# -- BEGIN
# --    SELECT
# user_id
# INTO
# usr_id
# FROM
# phone_book
# WHERE
# user_name = usr_name or user_surname = usr_surname;
#
# -- if usr_id
# IS
# NOT
# NULL
# THEN
# --        UPDATE
# phone_book
# --        SET
# phone_num = usr_phone_num
# WHERE
# id = user_id;
# --    ELSE
# --        INSERT
# INTO
# phone_book(user_name, user_surname, phone_num)
# --        VALUES(usr_name, usr_surname, usr_phone_num);
# --    END
# IF;
# -- END;
# -- $$
#
# -- CALL
# insert_user('new_user', 'new_user_surname', '102040506')
# -- SELECT * FROM
# phone_book;





except Exception as _ex:
    print("[INFO] Error working with PostgreSQL", _ex)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("[INFO] PostgreSQL closed successfully!")

        # CALL
        # insert_users(ARRAY['John Doe', 'Jane Smith', 'Bob Johnson'],
        #              ARRAY['+1-123-456-7890', '123-456-7890', '+1-1678977723-45-678'], CAST(NULL
        # AS
        # TEXT[]));
