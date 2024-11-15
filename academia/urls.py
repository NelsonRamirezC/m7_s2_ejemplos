from django.urls import path
from . import views

urlpatterns = [
    path('matricular/<int:estudiante_id>/', views.matricular, name='matricular'),
]