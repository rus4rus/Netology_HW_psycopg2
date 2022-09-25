import psycopg2
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')
user, password = config['DB']['login'], config['DB']['password']


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

def update(name, surname, email, changed_value, data_to_change):

    if changed_value not in ('name', 'surname', 'email'):
        print("Измененный параметр может быть только: 'name', 'surname' или 'email'! ")
        return

    try:
        conn = psycopg2.connect(database='clients', user=user, password=password)
        print('Соединение с базой открыто(изменение данных)')
        with conn.cursor() as cur:
            get_id = "SELECT id FROM Customer WHERE name = '%s' and surname = '%s' and email = '%s';" % (name, surname, email)
            cur.execute(get_id)
            id = cur.fetchone()
            if id:
                change_data_query = "UPDATE Customer SET %s = '%s' WHERE id = %s;" % (changed_value, data_to_change, id[0])
                cur.execute(change_data_query)
                conn.commit()
            else:
                print(f'Пользователя с именем "{name}", фамилией "{surname}", e-mail "{email}" не существует')
    except Exception as e:
        print(f'ERROR: {e}')
    finally:
        conn.close()
        print('Соединение с базой закрыто(добавление телефона)')




def remove_phone(name, surname, email, phone_number):
    try:
        conn = psycopg2.connect(database='clients', user=user, password=password)
        print('Соединение с базой открыто(удаление телефона)')
        with conn.cursor() as cur:
            get_id = "SELECT id FROM Customer WHERE name = '%s' and surname = '%s' and email = '%s';" % (name, surname, email)
            cur.execute(get_id)
            id = cur.fetchone()
            if id:
                delete_phone_query = "DELETE FROM Phone_numbers WHERE phone ='%s';" % (phone_number)
                cur.execute(delete_phone_query)
                conn.commit()
            else:
                print(f'Пользователя с именем "{name}", фамилией "{surname}", e-mail "{email}" не существует')
    except Exception as e:
        print(f'ERROR: {e}')
    finally:
        conn.close()
        print('Соединение с базой закрыто(удаление телефона)')

def remove_client(name, surname, email):

    try:
        conn = psycopg2.connect(database='clients', user=user, password=password)
        print('Соединение с базой открыто(удаление клиента)')
        with conn.cursor() as cur:
            get_id = "SELECT id FROM Customer WHERE name = '%s' and surname = '%s' and email = '%s';" % (name, surname, email)
            cur.execute(get_id)
            id = cur.fetchone()
            if id:
                remove_client_query = "DELETE from Customer WHERE id = '%s';" % (id[0])
                remove_phones_query = "DELETE from Phone_numbers WHERE customer_id = '%s';" % (id[0])
                cur.execute(remove_phones_query)
                cur.execute(remove_client_query)
                conn.commit()
            else:
                print(f'Пользователя с именем "{name}", фамилией "{surname}", e-mail "{email}" не существует')
    except Exception as e:
        print(e)
    finally:
        conn.close()
        print('Соединение с базой закрыто(удаление клиента)')


def find_client(name, surname, email):
    try:
        conn = psycopg2.connect(database='clients', user=user, password=password)
        print('Соединение с базой открыто(информация о клиенте)')
        with conn.cursor() as cur:
            get_info = "SELECT name, surname, email FROM Customer WHERE name = '%s' and surname = '%s' and email = '%s';" % (name, surname, email)
            get_id = "SELECT id FROM Customer WHERE name = '%s' and surname = '%s' and email = '%s';" % (name, surname, email)
            cur.execute(get_info)
            data_given = cur.fetchone()
            if get_id:
                name_given, surname_given, email_given = [*data_given]
                cur.execute(get_id)
                id = cur.fetchone()
                info_phone_query = "SELECT phone FROM Phone_numbers WHERE customer_id ='%s';" % (id[0])
                cur.execute(info_phone_query)
                phones = cur.fetchall()
                phone_given = ','.join([phone[0] for phone in phones]) or 'Нет телефона' #Если нет телефона, то надпись "Нет телефона"
                conn.commit()
                print(f'Имя: {name_given}, Фамилия:  {surname_given},  E-mail: {email_given},  Телефонные номера: {phone_given}')
            else:
                print(f'Пользователя с именем "{name}", фамилией "{surname}", e-mail "{email}" не существует')
    except Exception as e:
        print(f'ERROR: {e}')
    finally:
        conn.close()

        print('Соединение с базой закрыто(информация о клиенте)')

