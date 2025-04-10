

def test_get_tables(client, create_test_data):
    response = client.get("/tables/")
    assert response.status_code == 200
    tables = response.json()
    assert isinstance(tables, list)
    assert len(tables) > 0


def test_create_table(client, create_test_data):
    new_table_data = {
        "name": "Новая таблица",
        "seats": 6,
        "location": "VIP"
    }
    response = client.post("/tables/", json=new_table_data)
    assert response.status_code == 201
    assert response.json()["name"] == new_table_data["name"]
    assert response.json()["seats"] == new_table_data["seats"]
    assert response.json()["location"] == new_table_data["location"]


def test_delete_table(client, create_test_data):
    table_id = create_test_data.id
    response = client.delete(f"/tables/{table_id}")
    assert response.status_code == 204

    response = client.get(f"/tables/{table_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Столика с таким id не существует"


def test_delete_non_existent_table(client, create_test_data):
    non_existent_table_id = 999
    response = client.delete(f"/tables/{non_existent_table_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Столика с таким id не существует"
