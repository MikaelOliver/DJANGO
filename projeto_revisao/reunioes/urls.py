from django.urls import path, include
from rest_framework import routers
from .views import index, register,delete
from rest_framework import routers
from .api.viewsets import ReuniaoViewSet

router = routers.DefaultRouter()
router.register(r'reunioes', ReuniaoViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('delete/<int:id>', delete, name='delete'),
    path('register',register, name='register'),
    path('api_reunioes', include(router.urls)),
]
