from django.contrib import admin
from .models import Announcement, Item, Image, Comment, UserDetail

admin.site.register(Announcement)
admin.site.register(Item)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(UserDetail)
