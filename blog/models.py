from django.db import models
from django.urls import reverse
from labzlink import settings

class Post (models.Model):
    title = models.CharField (max_length=200)
    author = models.ForeignKey (settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    date = models.DateField (auto_now_add=True)
    text = models.TextField ()

    def __str__ (self):
        return self.title [:100]

    def get_absolute_url (self):
        return reverse ('post_detail', args=[str(self.id)])

