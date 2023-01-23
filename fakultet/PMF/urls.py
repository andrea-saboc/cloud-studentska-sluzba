from django.urls import path
from . import views

#all urls
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('register', views.index, name="register")
]