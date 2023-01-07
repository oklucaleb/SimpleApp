from django.urls import path
from sapp import views


urlpatterns = [
    path('',views.home,name='home'),
]