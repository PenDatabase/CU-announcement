"""
URL configuration for cu_announcement project.

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
from django.conf import settings
from django.views.generic import RedirectView



admin.site.site_header = "CU announcement"
admin.site.index_title = "Dev Admin"


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", RedirectView.as_view(url="/announcements/", permanent=False)), # redirect users to announcements/ when they request temporarily
    path('announcements/', include("announcements.urls")),
    path('user/', include("django.contrib.auth.urls")),
    path('user/', include("user.urls"))
]


if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls
    urlpatterns += debug_toolbar_urls()

