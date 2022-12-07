from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('index_2/', views.index_2),
    path('about_2/', views.about_2),
    path('contact_2/', views.contact_2),
]
