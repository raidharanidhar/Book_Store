from django.urls import path,include
# from .api import booklistapi,bookcreateapi,bookupdateapi,bookdeleteapi
from rest_framework.routers import DefaultRouter
from .api import BookViewSet
# urlpatterns=[
#     path("list/", booklistapi, name="booklist"),
#     path("create/", bookcreateapi, name="bookcreate"),
#     path("update/<int:id>", bookupdateapi, name="bookupdate"),
#     path("delete/<int:id>", bookdeleteapi, name="bookupdate"),

#  ]

router = DefaultRouter()
router.register('api', BookViewSet, basename='api')

urlpatterns = [
    path('', include(router.urls)),
]