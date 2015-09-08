import rest_service
import datetime
import urllib.error

""" Пример использования класса RestApi.
    У REST-сервиса не предусмотрен demo-режим, все действия совершаются в боевом режиме.
    То есть при вызове функции SendMessage сообщения реально отправляются.
    Будьте внимательны при вводе адреса отправителя и номеров получателей."""

login = 'логин'
password = 'пароль'
host = 'https://integrationapi.net/rest'

try:
    rest = rest_service.RestApi(login, password, host)
except urllib.error.URLError as error:
    print(error.code, error.msg)
    exit()
  
balance = rest.get_balance()
message_ids = rest.send_messages_bulk('адрес отправителя', ['номер получателя1', 'номер получателя2'], 'Hello, world!')
message_ids = rest.send_message('адрес отправителя', 'номер получателя', 'Hello, world!')
statistics = rest.get_statistics(datetime.date(2012, 3, 12), datetime.date(2012, 5, 8))
state = rest.get_message_state('WD1935D4E')

print(rest._session_id, balance, state)