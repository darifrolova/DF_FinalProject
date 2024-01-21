import configuration
import requests
import data

#Создание заказа
def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.header_content)

#Получение трека заказа
def create_order():
    current_body = data.order_content.copy()
    current_body["firstName"] = "Ivan"
    response = create_new_order(current_body)
    return str(response.json()["track"])

#Получение данных заказа по треку
def get_order(info):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params=info)