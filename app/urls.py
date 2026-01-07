from django.urls import path
from .views import CarListApiView, CarDetailApiView

urlpatterns = [
    path('cars/', CarListApiView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarDetailApiView.as_view(), name='car-detail'),
]
