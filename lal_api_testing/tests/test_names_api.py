import pytest
from rest_framework.test import APIClient
from api.models import Person

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_people(db):
    Person.objects.create(name="Alice")
    Person.objects.create(name="Bob")

@pytest.mark.django_db
def test_people_list(api_client, create_people):
    response = api_client.get("/api/names/")
    assert response.status_code == 200
    assert response.json() == {"people": ["Alice", "Bob"]}