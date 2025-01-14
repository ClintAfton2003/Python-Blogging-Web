from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('blog')
    
