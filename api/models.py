from django.db import models

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    author = models.CharField(max_length=50, default="Anonymous", blank=True)

    def __str__(self):
        return self.title