from django.shortcuts import render
from django.views import generic
from .models import Announcement
class IndexView(generic.ListView):
    queryset = Announcement.objects.all().order_by('-created_on')
    template_name = 'index.html'