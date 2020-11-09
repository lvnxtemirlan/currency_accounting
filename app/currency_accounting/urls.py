from django.urls import path

from . import views

urlpatterns = [
    path("currency/", views.page),
    path("currency/table/", views.show_table),
    path("currency/delete/<int:pk>", views.delete_table)
]