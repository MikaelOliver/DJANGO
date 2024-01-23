
from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'doadores', DoadoresViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('banco_de_sangue.urls'))
]
