import pytest
from board.models import Item
from django.urls import reverse


@pytest.mark.django_db
def test_items(client):
    response = client.get('items')
    assert response.status_code == 200

@pytest.mark.django_db
def test_items_form(client, item):
    response = client.post(reverse('items'), item)
    assert response.status_code == 302

    new_item = Item.objects.get()
    assert new_item.name == item.name
    assert new_item.description == item.description
    assert new_item.status == item.status

