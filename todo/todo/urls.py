

from django.contrib import admin
from django.urls import path, include
from todo_api import urls as todo_urls
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from todo_api import views




urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('auth/', include('djoser.urls')),

    path('auth/', include('djoser.urls.jwt')),

    path('api-auth/', include('rest_framework.urls')),

    path('todos/', include(todo_urls)),
    
]