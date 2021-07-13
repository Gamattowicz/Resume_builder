"""resume_builder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('personals/', include('personals.urls', namespace='personals')),
    path('skills/', include('skills.urls', namespace='skills')),
    path('hobby/', include('hobby.urls', namespace='hobby')),
    path('schools/', include('schools.urls', namespace='schools')),
    path('experiences/', include('experiences.urls', namespace='experiences')),
    path('resumes/', include('resumes.urls', namespace='resumes')),
    path('', include('api.urls', namespace='api')),
    path('', include('django.contrib.auth.urls')),
]
