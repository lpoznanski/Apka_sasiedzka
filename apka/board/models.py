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
    photo = models.ImageField(upload_to='media/items', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# class Image(models.Model):
#     pass
#
# class Comment(models.Model):
#     pass
#
# class UserDetail(models.Model):
#     pass