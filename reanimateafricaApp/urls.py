from django.urls import path
from . import views

urlpatterns = [
    path('', views. index),
    path('page', views. mainpage),
    # path('architecture', views. archi),
    # path('interior', views. inter),
    # path('furniture', views. furn),
    # path('3d', views. render),
]