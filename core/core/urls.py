"""
URL configuration for core project.
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the Smart Task API!",
        "version": "1.0.0",
        "endpoints": {
            "swagger_docs": "/api/schema/docs/",
            "redoc": "/api/schema/redoc/",
            "register": "/api/register/",
            "login": "/api/login/",
            "token_refresh": "/api/token/refresh/",
            "tasks": "/api/tasks/",
            "admin": "/admin/"
        }
    })

urlpatterns = [
    path('', api_root, name='api_root'),
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/tasks/', include('tasks.urls')),
    
    # API Documentation URLs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
