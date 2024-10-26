from django.urls import path
from profiles import views

urlpatterns = [
    path('create/', views.create_profile, name='create-profile'),
    path('details/', views.detailed_profile, name='detailed-profile'),
    path('edit/', views.edit_profile, name='edit-profile'),
    path('delete/', views.delete_profile, name='delete-profile'),

]