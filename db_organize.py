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
    MAKE_TABLE_CUSTOMER = 'CREATE TABLE IF NOT EXISTS Customer (id SERIAL PRIMARY KEY, name VARCHAR(40) not NULL, surname VARCHAR(40) not NULL, email VARCHAR(40) not NULL UNIQUE);'
    MAKE_TABLE_PHONE_NUMBERS = 'CREATE TABLE IF NOT EXISTS Phone_numbers (phone VARCHAR(20) primary KEY, customer_id INTEGER  REFERENCES Customer(id));'
    try:
        conn = psycopg2.connect(database='clients', user=user, password=password)
        print('Соединение с базой открыто(создание базы)')
        with conn.cursor() as cur:
            cur.execute(MAKE_TABLE_CUSTOMER)
            conn.commit()
            cur.execute(MAKE_TABLE_PHONE_NUMBERS)
            conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()
        print('Соединение с базой закрыто(создание базы)')

def add_client(name, surname, email, phone_number=''):
    add_client_query = "INSERT INTO Customer (name, surname, email) VALUES ('%s', '%s', '%s') RETURNING ID;" % (name, surname, email)
    try:
        conn = psycopg2.connect(database='clients', user=user, password=password)
        print('Соединение с базой открыто(добавление клиента)')
        with conn.cursor() as cur:
            cur.execute(add_client_query)
            id = cur.fetchone()[0]
            if phone_number:
                add_phone_query = "INSERT INTO Phone_numbers (phone, customer_id) VALUES ('%s', '%s');" % (phone_number, id)
                cur.execute(add_phone_query)

            conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()
        print('Соединение с базой закрыто(добавление клиента)')


def add_phone(name, surname, email, phone_number):

    try:
        conn = psycopg2.connect(database='clients', user=user, password=password)
        print('Соединение с базой открыто(добавление телефона)')
        with conn.cursor() as cur:
            get_id = "SELECT id FROM Customer WHERE name = '%s' and surname = '%s' and email = '%s';" % (name, surname, email)
            cur.execute(get_id)
            id = cur.fetchone()
            if id:
                add_phone_query = "INSERT INTO Phone_numbers (phone, customer_id) VALUES ('%s', '%s');" % (phone_number, id[0])
                cur.execute(add_phone_query)
                conn.commit()
            else:
                print(f'Пользователя с именем "{name}", фамилией "{surname}", e-mail "{email}" не существует')
    except Exception as e:
        print(f'ERROR: {e}')
    finally:
        conn.close()
        print('Соединение с базой закрыто(добавление телефона)')

def update():
    pass

def remove_phone():
    pass

def remove_client():
    pass

def find_client():
    pass


# create_table()
# add_client('Vasyan', 'Petrov', 'Vavasy3@mail.ru','+791243439')
add_phone('Vasyan', 'Petrov', 'Vavasy3@mail.ru','+800889--0r0w')