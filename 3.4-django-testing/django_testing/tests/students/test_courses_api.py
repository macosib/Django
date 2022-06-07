import pytest
from rest_framework.test import APIClient

from students.models import Course, Student

@pytest.fixture
def client():
    return APIClient()

@pytest.mark.django_db
def test_example(client):
    #Arrange

    # Act
    responce = client.get('/api/v1/courses/')


    #Assert
    assert responce.status_code == 200
    data = responce.json()
    assert len(data) == 1

