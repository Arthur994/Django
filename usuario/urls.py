
from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('registrar/', views.register.as_view(), name='registrar'),
]