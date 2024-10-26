from django.urls import path, include
from cars import views

urlpatterns = [
    path('catalogue/', views.catalogue, name='catalogue'),

]