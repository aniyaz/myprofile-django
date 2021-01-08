from django.urls import path

from aprofile import views

urlpatterns = [
    path("", views.index, name="index")
]
