from django.urls import path
from .api import booklistapi,bookcreateapi,bookupdateapi,bookdeleteapi

urlpatterns=[
    path("list/", booklistapi, name="booklist"),
    path("create/", bookcreateapi, name="bookcreate"),
    path("update/<int:id>", bookupdateapi, name="bookupdate"),
    path("delete/<int:id>", bookdeleteapi, name="bookupdate"),

 ]