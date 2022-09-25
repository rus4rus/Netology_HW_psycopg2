# Домашнее задание к лекции «Работа с PostgreSQL из Python»

Создайте программу для управления клиентами на python.

Требуется хранить персональную информацию о клиентах:

- имя
- фамилия
- email
- телефон

Сложность в том, что телефон у клиента может быть не один, а два, три и даже больше. А может и вообще не быть телефона (например, он не захотел его оставлять).

Вам необходимо разработать структуру БД для хранения информации и несколько функций на python для управления данными:

1. Функция, создающая структуру БД (таблицы)
1. Функция, позволяющая добавить нового клиента
1. Функция, позволяющая добавить телефон для существующего клиента
1. Функция, позволяющая изменить данные о клиенте
1. Функция, позволяющая удалить телефон для существующего клиента
1. Функция, позволяющая удалить существующего клиента
1. Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)

Функции выше являются обязательными, но это не значит что должны быть только они. При необходимости можете создавать дополнительные функции и классы.

Также предоставьте код, демонстрирующий работу всех написанных функций.

Результатом работы будет `.py` файл.

ВАЖНО:
Доступ к информации осуществляется строго по 3 параметрам: Имя, Фамилия, E-mail, где E-mail - уникально.
В функции "update" указываем измененный параметр среди данных:'name', 'surname' или 'email'
