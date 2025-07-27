from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('record-login/', views.record_login_attempt, name='record_login'),
    

]