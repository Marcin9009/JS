from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase


CREATE_DB = "CREATE DATABASE library_db;"
"""Create database"""

CREATE_TABLE_AUTOR = """CREATE TABLE autor(
    id serial PRIMARY KEY,
    name varchar(80));"""

CREATE_TABLE_BOOK = """CREATE TABLE book(
    id serial PRIMARY KEY,
    ISBN varchar(13),
    name text,
    is_loande = FALSE);"""

CREATE_TABLE_CLIENT = """CREATE TABLE client(
    id serial PRIMARY KEY,
    first_name varchar(80),
    last_name varchar(80));"""


USER = "postgres"
PASSWORD = "coderslab"
HOST = "127.0.0.1"
DATEBASE = "library_db"


try:
    cnx = connect(user=USER, password=PASSWORD, host=HOST, database=DATEBASE)
    cnx.autocommit = True
    cnx = cnx.cursor()
    try:
        cursor.execute(DATEBASE)
        print("Create database")
    except DuplicateDatabase as o:
        print("exist database", o)

        try:
            cursor.execute(CREATE_TABLE_AUTOR)
            print("Create table")
        except DuplicateDatabase as d:
            print("exist database", )
        try:
            cuursore




cnx.close()




