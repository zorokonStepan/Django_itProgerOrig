from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_3, name='index_3'),
    path('about_3/', views.about_3, name='about_3'),
    path('contact_3/', views.contact_3, name='contact_3'),

    path('index_2/', views.index_2, name='index_2'),
    path('about_2/', views.about_2, name='about_2'),
    path('contact_2/', views.contact_2, name='contact_2'),

    path('index_1/', views.index_1),
    path('about_1/', views.about_1),
    path('contact_1/', views.contact_1),
]
