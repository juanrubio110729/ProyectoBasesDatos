from django.contrib import admin
from user.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType



# Register your models here.
admin.site.register(User)
admin.site.register(Permission)
admin.site.register(ContentType)