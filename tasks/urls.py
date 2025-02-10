from django.urls import path

from .views import manager_dashboard, user_dashboard, test, create_task, view_task


urlpatterns = [
    path('manager-dashboard/', manager_dashboard, name="manager-dashboard"),
    path('user-dashboard/', user_dashboard),
    path('test/', test),
    path('create-task/', create_task, name='create-task'),
    path('view-task/', view_task)
] 