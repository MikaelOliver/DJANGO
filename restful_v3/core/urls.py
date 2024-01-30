
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pontos_turisticos.urls')),
    path('atracoes_turisticos', include('atracoes_turisticos.urls'))
]
