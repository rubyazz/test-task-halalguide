import pytest
from points.models import PointOfInterest
from rest_framework import status
from rest_framework.test import APIClient


@pytest.fixture
def create_poi():
    """
    Fixture to create a Point of Interest before each test
    """
    poi_data = {
        "name": "Test Point of Interest",
        "latitude": 37.7749,
        "longitude": -122.4194,
        "description": "A test POI in San Francisco.",
    }
    poi = PointOfInterest.objects.create(**poi_data)
    return poi


@pytest.fixture
def client():
    """
    Fixture to initialize the APIClient
    """
    return APIClient()


@pytest.mark.django_db
def test_create_poi(client):
    """
    Ensure we can create a new PointOfInterest object.
    """
    poi_data = {
        "name": "Test Point of Interest",
        "latitude": 37.7749,
        "longitude": -122.4194,
        "description": "A test POI in San Francisco.",
    }
    url = "/api/point/"

    response = client.post(url, poi_data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert PointOfInterest.objects.count() == 1
    assert (
        PointOfInterest.objects.get(id=response.data["id"]).name
        == "Test Point of Interest"
    )


@pytest.mark.django_db
def test_read_poi(client, create_poi):
    """
    Ensure we can retrieve the PointOfInterest we created.
    """
    url = f"/api/point/{create_poi.id}/"
    response = client.get(url, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == create_poi.name
    assert response.data["latitude"] == create_poi.latitude
    assert response.data["longitude"] == create_poi.longitude


@pytest.mark.django_db
def test_update_poi(client, create_poi):
    """
    Ensure we can update a PointOfInterest.
    """
    updated_data = {
        "name": "Updated Point of Interest",
        "latitude": 37.7749,
        "longitude": -122.4194,
        "description": "Updated description.",
    }
    url = f"/api/point/{create_poi.id}/"

    response = client.put(url, updated_data, format="json")

    assert response.status_code == status.HTTP_200_OK
    create_poi.refresh_from_db()
    assert create_poi.name == "Updated Point of Interest"
    assert create_poi.description == "Updated description."


@pytest.mark.django_db
def test_delete_poi(client, create_poi):
    """
    Ensure we can delete a PointOfInterest.
    """
    url = f"/api/point/{create_poi.id}/"

    response = client.delete(url, format="json")

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert PointOfInterest.objects.count() == 0


@pytest.mark.django_db
def test_list_pois(client, create_poi):
    """
    Ensure we can list all PointOfInterest objects.
    """
    url = "/api/point/"

    response = client.get(url, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0
