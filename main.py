import pytest
import requests

# Конфигурация API
BASE_URL = "https://reqres.in/api"
API_KEY = "reqres_ce5bd0562a3642c6ba87630e2aa3f9ea"
HEADERS = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}


def test_get_user():
    """GET: Получить пользователя с ID=2 и проверить email"""
    response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS)

    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"

    data = response.json()
    assert "data" in data, "Ответ не содержит ключ 'data'"
    assert "email" in data["data"], "Поле 'email' отсутствует в данных пользователя"
    assert "@" in data["data"]["email"], "Email не содержит символ '@'"


def test_create_user():
    """POST: Создать пользователя Vlad / analyst"""
    payload = {"name": "Vlad", "job": "analyst"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)

    assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"

    data = response.json()
    assert data["name"] == "Vlad"
    assert data["job"] == "analyst"
    assert "id" in data
    assert "createdAt" in data


def test_update_user():
    """PUT: Обновить пользователя ID=2 на Vlad / analyst"""
    payload = {"name": "Vlad", "job": "analyst"}
    response = requests.put(f"{BASE_URL}/users/2", json=payload, headers=HEADERS)

    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"

    data = response.json()
    assert data["name"] == "Vlad"
    assert data["job"] == "analyst"
    assert "updatedAt" in data