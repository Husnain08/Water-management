from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name = 'index'),
  #  path('' , views.data_vis_height , name = 'data_vis'),
   # path('' , views.data_vis_height , name = 'data_vis_height'),

]

