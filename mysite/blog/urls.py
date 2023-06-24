from django.urls import path
from . import views
urlpatterns = [
    path("", views.principale, name="principale"),
    path("blog" , views.blog, name="blogpage"),
    path("blog/<slug:slug>", views.blogdetails, name="blogdetailspage")
]
