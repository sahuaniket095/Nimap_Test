from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Client, Project
from .serializers import Client_Serializer, Client_Detail_Serializer, Project_Serializer, Project_Create_Serializer


class Client_List_Create_View(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = Client_Serializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)



class Client_Retrieve_Update_Delete_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = Client_Detail_Serializer
    permission_classes = [IsAuthenticated]


class Project_CreateForClient_View(generics.CreateAPIView):
    serializer_class = Project_Create_Serializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
       
        client_id = self.kwargs.get('client_id')
        client = get_object_or_404(Client, id=client_id)

       
        project = serializer.save(client=client, created_by=self.request.user)

       
        project.users.set(serializer.validated_data.get('users', []))


class User_Projects_List_View(generics.ListAPIView):
    serializer_class = Project_Serializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)
