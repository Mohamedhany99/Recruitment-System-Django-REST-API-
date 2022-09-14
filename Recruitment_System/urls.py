"""Recruitment_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

import hr_management.api_view
import hr_management.views

urlpatterns = [
    path('api/v1/emp/',hr_management.api_view.EmpList.as_view()),
    path('api/v1/emp/create/',hr_management.api_view.EmpCreate.as_view()),
    path('api/v1/emp/<int:id>/',hr_management.api_view.EmpRetrieveUpdateDestroy.as_view()),

    path('', hr_management.views.index, name='Employee-login'),


    path('admin/', admin.site.urls),
]
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
