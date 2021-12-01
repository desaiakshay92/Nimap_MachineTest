from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

# Create your models here.
class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=50,blank=False)
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.created_by

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50)
    client = models.ForeignKey("Client",on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.project_name

class User(AbstractUser):
    username=None
    email = models.EmailField(unique=True)
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    project = models.ManyToManyField("Project",related_name='users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    


    