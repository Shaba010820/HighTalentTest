

def test_get_reservations(client):
    response = client.get("/reservs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_reservation(client):
    reservation_data = {
        "customer_name": "Ronaldinho",
        "table_id": 1,
        "reservation_time": "2025-04-10T18:00:00",
        "duration_minutes": 120
    }
    response = client.post("/reservs/", json=reservation_data)
    assert response.status_code == 201
    assert response.json()["customer_name"] == "Ronaldinho"


def test_reservation_intersection(client):
    reservation_data_1 = {
        "customer_name": "User 1",
        "table_id": 1,
        "reservation_time": "2025-04-10T18:00:00",
        "duration_minutes": 120
    }
    response1 = client.post("/reservs/", json=reservation_data_1)
    assert response1.status_code == 201
    reservation_data_2 = {
        "customer_name": "User 2",
        "table_id": 1,
        "reservation_time": "2025-04-10T19:00:00",
        "duration_minutes": 120
    }
    response2 = client.post("/reservs/", json=reservation_data_2)
    assert response2.status_code == 400
    assert response2.json().get("detail") == "Стол уже забронирован на этот период времени"
