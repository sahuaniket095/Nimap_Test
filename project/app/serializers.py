from rest_framework import serializers
from .models import Client, Project



class Project_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'created_at', 'created_by']

class Project_Create_Serializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    

    class Meta:
        model = Project
        fields = [
            'id',
            'project_name',
            'client',
            'users',
            'created_at',
            'created_by'
        ]

        read_only_fields = ['client', 'created_at', 'created_by']

class Client_Serializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'updated_at']


class Client_Detail_Serializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'updated_at']
