from db_organize import create_table, add_client, add_phone, update, remove_phone, remove_client, find_client

'''
Создайте программу для управления клиентами на python.

Требуется хранить персональную информацию о клиентах:

    имя
    фамилия
    email
    телефон

Сложность в том, что телефон у клиента может быть не один, а два, три и даже больше. А может и вообще не быть телефона (например, он не захотел его оставлять).

Вам необходимо разработать структуру БД для хранения информации и несколько функций на python для управления данными:

Функция, создающая структуру БД (таблицы)
Функция, позволяющая добавить нового клиента
Функция, позволяющая добавить телефон для существующего клиента
Функция, позволяющая изменить данные о клиенте
Функция, позволяющая удалить телефон для существующего клиента
Функция, позволяющая удалить существующего клиента
Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)

ВАЖНО:
Доступ к информации осуществляется строго по 3 параметрам: Имя, Фамилия, E-mail, где E-mail - уникально.
В функции "update" указываем измененный параметр:'name', 'surname' или 'email'
'''
if __name__ == '__main__':
    create_table()
    add_client('Vasya', 'Vasin', 'Vasya@mail.ru','+791243439')
    add_client('Petya', 'Petrov', 'Petya@mail.ru','+791243569')
    add_client('Kolya', 'Kolin', 'Kolya@mail.ru')
    add_phone('Vasya', 'Vasin', 'Vasya@mail.ru','+800889657')
    add_phone('Vasya', 'Vasin', 'Vasya@mail.ru','+84564556346354')
    update(name='Petya', surname='Petrov', email='Petya@mail.ru', changed_value='name', data_to_change='Petya_modified')
    remove_phone('Vasya', 'Vasin', 'Vasya@mail.ru', '+791243439')
    remove_phone('Kolya', 'Kolin', 'Kolya@mail.ru', '+7912434349') #удаляем несуществующий телефон
    remove_client('Petya_modified', 'Petrov', 'Petya@mail.ru')
    find_client('Vasya', 'Vasin', 'Vasya@mail.ru')
    find_client('Kolya', 'Kolin', 'Kolya@mail.ru')