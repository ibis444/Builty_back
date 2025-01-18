from django.urls import path
from . import views
app_name = 'info'
urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
]
