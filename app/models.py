from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    address=models.TextField(max_length=200)
    profile_pic=models.ImageField(upload_to='profilePics')
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    