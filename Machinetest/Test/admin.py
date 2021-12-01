from django.contrib import admin
from Test.models import Client,Project,User

# Register your models here.
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(User)