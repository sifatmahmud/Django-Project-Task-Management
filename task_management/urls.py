
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from tasks.views import manager_dashboard


urlpatterns = [
    path("", manager_dashboard, name="home"),
    path('admin/', admin.site.urls),
    path("tasks/", include("tasks.urls"))
]+ debug_toolbar_urls()
