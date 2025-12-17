import json
import os
import sys

# Asegurar que el paquete raíz esté en el path para importar `app`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app


def test_index():
    app = create_app()
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json() == {"message": "Hola desde Flask!"}


def test_create_and_get_items():
    app = create_app()
    client = app.test_client()

    res = client.get("/items")
    assert res.status_code == 200
    initial = res.get_json()

    res = client.post("/items", json={"name": "nuevo"})
    assert res.status_code == 201
    created = res.get_json()
    assert created["name"] == "nuevo"

    res = client.get("/items")
    assert any(i["name"] == "nuevo" for i in res.get_json())
