from django.urls import path
from .views import gallery_view,addPhoto_view,photo_view

urlpatterns = [
    path("", gallery_view, name="gallery"),
    path("add/", addPhoto_view, name="add"),
    path("photo/<int:id>", photo_view, name="photo"),
]
