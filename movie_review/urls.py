from django.urls import path
from . import views

app_name = 'movie_review'

urlpatterns = [
    path("", views.index, name='index'),
    path("new/", views.new, name="new"),
    path("create/", views.create, name='create'),
    path("detail/<int:review_pk>", views.detail, name='detail'),
    path("edit/<int:review_pk>", views.edit, name='edit'),
    path("modify/<int:review_pk>", views.modify, name="modify"),
    path("delete/<int:review_pk>", views.delete, name="delete"),
]
