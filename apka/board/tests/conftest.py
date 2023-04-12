import pytest
from django.test import Client
from board.models import Item
from django.contrib.auth.models import User
@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def item():
    user = User.objects.first()
    return Item.objects.create(author=user, status='1', name='name', description='description')
