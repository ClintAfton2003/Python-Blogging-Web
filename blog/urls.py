from django.urls import path
from . import views

urlpatterns = [
    path('', views.list),
    path('<int:id>/', views.post),
    path("add_blog/", views.add_blogs, name="add_blog"),
]
