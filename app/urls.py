from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.signin.as_view(), name='login'),
    path('logout/', views.signout, name='logout'),
    path('register/', views.register.as_view(), name='register'),
    path('users/', views.users.as_view(), name='users'),
    path('results', views.results.as_view(), name='results')
]
