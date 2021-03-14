from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce import HTMLField

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField()

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=True, blank=True)
    featured = models.BooleanField()
    content = HTMLField(default='NO CONTENT DEFAULT SYSTEM')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog', kwargs={
            'blog_id': self.id
        })
