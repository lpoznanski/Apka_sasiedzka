from django import forms
from .models import Item, UserDetail, Comment


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ["author"]

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'