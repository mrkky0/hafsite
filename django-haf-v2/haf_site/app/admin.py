from django.contrib import admin

# Register your models here.
from .models import Products,Category  # YourModelName, eklemek istediğiniz modelin adı olmalı

admin.site.register(Products)
admin.site.register(Category)