import pytest
from fastapi import status
from httpx import AsyncClient
from main import app

BASE_URL = "http://localhost:8000"

@pytest.mark.asyncio
async def test_fetch_users():
    async with AsyncClient(app=app, base_url=BASE_URL) as client:
        response = await client.get("/api/v1/users")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["status"] == "success"
        assert "data" in data


# @pytest.mark.asyncio
# async def test_create_user():
#     async with AsyncClient(app=app, base_url=BASE_URL) as client:
#         user_data = {
#             "id": "testid",
#             "username": "testusername1",
#             "password": "testpassword1"
#         }
#         response = await client.post("/api/v1/register", json=user_data)
#         assert response.status_code == status.HTTP_201_CREATED
#         data = response.json()
#         assert data["status"] == "success"
#         assert "data" in data


@pytest.mark.asyncio
async def test_login():
    async with AsyncClient(app=app, base_url=BASE_URL) as client:
        user_data = {
            "username": "John",
            "password": "Doe"
        }
        response = await client.post("/api/v1/login", json=user_data)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["status"] == "success"
        assert "data" in data
        assert "token" in data
