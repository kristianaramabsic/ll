from django.db import models

class Post (models.Model):
    title = models.CharField (max_length=200)
    author = models.ForeignKey ('auth.User', on_delete=models.CASCADE,)
    date = models.DateField (auto_now_add=True)
    text = models.TextField ()

    def __str__ (self):
        return self.title [:100]

