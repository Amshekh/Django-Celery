from django.urls import path
from celeryappone import views

urlpatterns = [
    path('', views.index, name='home'),
    path('product/', views.product, name='product'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('res/<str:task_id>', views.check_res, name='check_res')
]
