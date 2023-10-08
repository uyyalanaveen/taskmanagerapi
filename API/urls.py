from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Taskview

route = DefaultRouter()
route.register('api',Taskview, basename='taskview')
urlpatterns = [
    path('',include(route.urls))
]
