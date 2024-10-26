from django.urls import path, include
from cars import views

urlpatterns = [
    path('catalogue/', views.catalogue, name='catalogue'),
    path('create/', views.create_car, name='create-car'),
    path('<int:id>/', include([
        path('details/', views.detailed_car, name='detailed-car'),
        path('edit/', views.edit_car, name='edit-car'),
        path('delete/', views.delete_car, name='delete-car')
    ]))


]