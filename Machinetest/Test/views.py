from django.shortcuts import render
from rest_framework import viewsets
from Test.models import Client,Project,User
from Test.serializer import ClientSerializer, ProjectSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.
class ClientViewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    permission_classes_by_action = {'list':[IsAdminUser]}
    
    def list(self, request, *args, **kwargs):
        return super(ProjectViewset, self).list(request,*args, **kwargs)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
            
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
