from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.allarticles, name='allarticles'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
