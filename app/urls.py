from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('one',views.alltodos,name='alltodos'),
    path('two/<int:pk>' ,views.todolists,name = 'todolists'),
    path('three/<int:pk>',views.edit,name='edit'),
    path('four/<int:jp>',views.list,name='list'),
    path('his',views.list,name='read'),
    ]
