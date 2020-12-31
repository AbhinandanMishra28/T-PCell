from django.contrib import admin

# Register your models here.
from .models import Register_Model, Author

admin.site.register(Register_Model)