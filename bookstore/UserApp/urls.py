from django.urls import path
from .apis import UserCreateApi,ProtectedView

urlpatterns=[
    path('create/',UserCreateApi),
    # path('login/',UserLoginApi),
    path('protected',ProtectedView)
 ]