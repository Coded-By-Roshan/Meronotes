from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('' , views.home_view , name="home"),
    path('note' , views.note_view , name="note"),
    path('contact' , views.contact_view , name="contact"),
    path('feed' , views.feedBack_view , name="feed"),
    path('details/<int:pk>' , views.detial_view , name="detail"),
    path('login' , views.login_view , name="login"),
    path('add_notes' , views.addNote_view , name="add_notes"),
    path('send/contact' , views.managecontact , name="manageContact"),
    path('search' , views.search_view , name="search"),
    # path('Page_Not_Found' , views.Page_Not_Found , name="Page_Not_Found"),
]
