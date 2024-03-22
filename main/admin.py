from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Region)
admin.site.register(models.Post)
admin.site.register(models.PostImage)
admin.site.register(models.PostVideo)
admin.site.register(models.Comment)
