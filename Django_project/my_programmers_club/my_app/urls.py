from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("members/", views.members, name="members"),
    path("members/details/<slug:slug>", views.details, name="details"),
    path("add_member/", views.add_member, name="add_member"),
    path("member/delete/<slug:slug>", views.delete_member, name="delete_member"),
    path("member/update/<slug:slug>", views.update_member, name="update_member"),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]
