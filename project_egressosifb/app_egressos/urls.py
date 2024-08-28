from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('questionario/', views.questionario_view, name='questionario'),
]

