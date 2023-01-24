from django.urls import path
from . import views

#all urls
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('registerp', views.register_professor, name="registerp"),
    path('register', views.index, name="register"),
]