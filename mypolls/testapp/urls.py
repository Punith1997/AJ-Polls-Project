from django.urls import path
from testapp import views

app_name='testapp'

urlpatterns = [
    path('', views.homeview,name='home'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('signup/', views.signupview, name='signup'),
    path('password/', views.change_password, name='change_password'),
]
