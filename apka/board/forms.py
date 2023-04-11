from django import forms
from .models import Item, UserDetail


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ["author"]

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = '__all__'