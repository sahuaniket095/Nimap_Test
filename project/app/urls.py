from django.urls import path
from .views import Client_List_Create_View, Client_Retrieve_Update_Delete_View, Project_CreateForClient_View, User_Projects_List_View


urlpatterns = [
    path('clients/', Client_List_Create_View.as_view(), name='client-list-create'),

    path('clients/<int:pk>/', Client_Retrieve_Update_Delete_View.as_view(), name='client-detail'),

    path('clients/<int:client_id>/projects/', Project_CreateForClient_View.as_view(), name='client-project-create'),
    
    path('projects/', User_Projects_List_View.as_view(), name='user-projects'),
]
