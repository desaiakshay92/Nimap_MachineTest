from django.shortcuts import render
from rest_framework import viewsets
from Test.models import Client,Project,User
from Test.serializer import ClientSerializer, ProjectSerializer, UserSerializer

# Create your views here.
class ClientViewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
