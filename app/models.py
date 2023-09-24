from django.db import models
from PIL import Image
from .utility import *
from django.contrib.auth.models import User


# Create your models here.
class user_profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    security_qus = models.CharField(max_length= 100)
    ans = models.CharField(max_length= 50)
    
    def __str__(self):
        return str(self.user)


class image_denoising(models.Model):
    image = models.ImageField()
    denoised_image = models.CharField(max_length= 500)
    date = models.DateField()

        
    def __str__(self) -> str:
        return super().__str__()