# Фролова Дарья, 12-я когорта - Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_requests

def positive_assert():
    track_number = sender_stand_requests.create_order()
    current_params = data.params_track.copy()
    current_params["t"] = track_number
    order_response = sender_stand_requests.get_order(current_params)
    assert order_response.status_code == 200
    assert order_response.json()["order"] != ""

def test_order():
    positive_assert()