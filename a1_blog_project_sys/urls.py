"""
URL configuration for a1_blog_project_sys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


from rest_framework.documentation import include_docs_urls # new
schema_view = get_schema_view(title='Blog Project API')



urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/posts/', include('posts.api.urls')),
    path('api/humans/', include('humans.api.urls')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # just brouserble apis( for development only )
    path('api/', include('dj_rest_auth.urls')),  # login, logout, password reset etc (real production)

    path('api/reg/', include('dj_rest_auth.registration.urls')), #for registration

    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    # Serves Swagger UI
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]
