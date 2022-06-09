import pytest
from rest_framework.test import APIClient
from students.models import Course, Student
from model_bakery import baker
from random import randint


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def factory_course():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def factory_student():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_one_course(client, factory_course):
    courses = factory_course(_quantity=5)
    responce = client.get('/api/v1/courses/3/')
    data = responce.json()
    assert responce.status_code == 200
    assert courses[2].name == data['name']


@pytest.mark.django_db
def test_get_list_course(client, factory_course):
    courses = factory_course(_quantity=5)
    responce = client.get('/api/v1/courses/')
    data = responce.json()
    assert responce.status_code == 200
    assert len(data) == len(courses)
    for index, course in enumerate(data):
        assert course['name'] == courses[index].name


#
@pytest.mark.django_db
def test_get_filter_id_course(client, factory_course):
    courses = factory_course(_quantity=5)
    id_course = courses[0].id
    responce = client.get(f'/api/v1/courses/?id={id_course}')
    data = responce.json()
    assert responce.status_code == 200
    assert id_course == data[0]['id']


@pytest.mark.django_db
def test_get_filter_name_course(client, factory_course):
    courses = factory_course(_quantity=5)
    name = courses[0].name
    responce = client.get(f'/api/v1/courses/?name={name}')
    data = responce.json()
    assert responce.status_code == 200
    assert name == data[0]['name']



@pytest.mark.django_db
def test_get_create_course(client):
    count = Course.objects.count()
    data = {'name': 'TestCourse'}
    responce = client.post('/api/v1/courses/', data=data)
    assert responce.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_get_patch_course(client, factory_course):
    courses = factory_course(_quantity=5)
    id_course = courses[0].id
    data = {'name': 'patch_name'}
    responce = client.patch(f'/api/v1/courses/{id_course}/', data=data)
    assert responce.status_code == 200
    assert Course.objects.filter(id=id_course)[0].name == data['name']


@pytest.mark.django_db
def test_get_delete_course(client, factory_course):
    courses = factory_course(_quantity=5)
    id_course = courses[0].id
    print(courses)
    print(courses)
    count = Course.objects.count()
    responce = client.delete(f'/api/v1/courses/{id_course}/')
    assert responce.status_code == 204
    assert count - 1 == Course.objects.count()
