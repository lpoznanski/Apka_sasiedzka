from django.shortcuts import render
from django.views import generic
from .models import Announcement, Item
class IndexView(generic.ListView):
    queryset = Announcement.objects.all().order_by('-created_on')
    template_name = 'index.html'

class PostDetailView(generic.DetailView):
    model = Announcement
    template_name = 'post_detail.html'

class ItemListView(generic.ListView):
    queryset = Item.objects.all().order_by('-created_on')
    template_name = 'item_list.html'