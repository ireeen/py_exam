import pytest
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

@pytest.mark.django_db
def test_product(client):
    response = client.get('/shop/products/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_category(client):
    response = client.get('/shop/categories/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_cart(client):
    response = client.get('/shop/cart/')
    assert response.status_code == 401


@pytest.mark.django_db
def test_order(client):
    response = client.get('/shop/order/')
    assert response.status_code == 401