from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField
    Author = models.ForeignKey(get_user_model())
    Created_date = models.DateTimeField(auto_now_add= True, null= True)
    Published_date = models.DateTimeField(auto_now_add= True, null= True)

    def __str__(self) -> str:
        return self.name