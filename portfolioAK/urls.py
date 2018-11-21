"""portfolioAK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import projects.views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', projects.views.homepage, name='home'),
    path('',include('contact.urls')),
    path('home/', projects.views.homepage, name='home'),
    path('summernote/', include('django_summernote.urls')),
    path('article/', include('article.urls'), name='article'),
    path('contact/', include('contact.urls'), name='contact'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
