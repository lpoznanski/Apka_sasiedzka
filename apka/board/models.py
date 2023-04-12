from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Announcement(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Announcement, self).save()


STATUS_CHOICES = (
    ('1', 'zgubione'),
    ('2', 'znalezione')
)

class Item(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1')
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='photos')
    photo = models.FileField(upload_to='media/items', null=True, blank=True)

class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=9, blank=True)
    facebook_profile = models.CharField(max_length=255)
