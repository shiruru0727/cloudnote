from django.contrib import admin

# Register your models here.
from note import models

admin.site.register(models.Note)