from django.urls import path

from . import views

app_name = 'core_functionality'

urlpatterns = [
    path('', views.index, name='index'),
]
