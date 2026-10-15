from Home.routers import urlpatterns as api_urlpatterns
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
    path('api-auth/', include('rest_framework.urls')),
]

