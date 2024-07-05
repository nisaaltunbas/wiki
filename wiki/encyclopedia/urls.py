from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.entry, name="entry"),
    path("search/",views.search,name="search"),
    path("newpage/",views.new_page,name="new_page"),
    path("edit/",views.edit,name="edit"),
    path("edit_view/",views.edit_view,name="edit_view"),
    path("random/",views.random,name="random")
]
