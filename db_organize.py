# Создайте программу для управления клиентами на python.
#
# Требуется хранить персональную информацию о клиентах:
#
#     имя
#     фамилия
#     email
#     телефон
#
# Сложность в том, что телефон у клиента может быть не один, а два, три и даже больше. А может и вообще не быть телефона (например, он не захотел его оставлять).
#
# Вам необходимо разработать структуру БД для хранения информации и несколько функций на python для управления данными:
#
#     Функция, создающая структуру БД (таблицы)
#     Функция, позволяющая добавить нового клиента
#     Функция, позволяющая добавить телефон для существующего клиента
#     Функция, позволяющая изменить данные о клиенте
#     Функция, позволяющая удалить телефон для существующего клиента
#     Функция, позволяющая удалить существующего клиента
#     Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)

import psycopg2
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')
user,password = config['DB']['login'], config['DB']['password']




def create_table():
    MAKE_TABLE_CUSTOMER = 'CREATE TABLE IF NOT EXISTS Customer (id SERIAL PRIMARY KEY, name VARCHAR(40) not NULL, surname VARCHAR(40) not NULL, email VARCHAR(40) not NULL);'
    MAKE_TABLE_PHONE_NUMBERS = 'CREATE TABLE IF NOT EXISTS Phone_numbers (phone VARCHAR(20) primary KEY, customer_id INTEGER  REFERENCES Customer(id));'
    try:
        conn = psycopg2.connect(database='clients', user=user, password=password)
        with conn.cursor() as cur:
            cur.execute(MAKE_TABLE_CUSTOMER)
            conn.commit()
            cur.execute(MAKE_TABLE_PHONE_NUMBERS)
            conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()
        print('Соединение с базой закрыто')


create_table()