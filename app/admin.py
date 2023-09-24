from django.contrib import admin
from .models import image_denoising, user_profile
# Register your models here.

admin.site.register(image_denoising)
admin.site.register(user_profile)