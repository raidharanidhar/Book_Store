from django.urls import path
from .apis import *

urlpatterns=[
    path('create/',UserCreateApi),
    path('login/',UserLoginApi),
    path('protected',ProtectedView)
 ]