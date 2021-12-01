from rest_framework import serializers
from Test.models import Client,Project,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id','name']

class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True,read_only=True)
    class Meta:
        model = Project
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True,read_only=True)
    class Meta:
        model = Client
        fields = '__all__'

