from django.urls import path
from . import views

urlpatterns= [
    path('', views.home_page, name="home_page"),
    path('thank_you', views.thank_you, name="thank_you"),
]
