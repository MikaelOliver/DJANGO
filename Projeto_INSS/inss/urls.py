from django.urls import path, include
from rest_framework import routers
from .api.viewsets import MeuInssViewSet

router = routers.DefaultRouter()
router.register(r'meuinss',MeuInssViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
