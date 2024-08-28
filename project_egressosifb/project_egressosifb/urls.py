from django.contrib import admin
from django.urls import path
from app_egressos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  # Redireciona a raiz para a tela de login
    path('login/', views.login_view, name='login'),
    path('questionario/', views.questionario_view, name='questionario'),
]
