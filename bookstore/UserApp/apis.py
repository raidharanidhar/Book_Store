from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required  # ✅ correct
from django.contrib.auth import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import *
# from rest_framework.python
@login_required
@api_view(['POST'])
def UserCreateApi(request):
    username=request.data['username']
    password=request.data['password']
    
    # User(username=username, password=password).save()
    
    User.objects.create_user(username=username, password=password)
    return Response({
        "message": "User created successfully"
    })

@csrf_exempt
@api_view(['POST'])
def UserLoginApi(request):
    username=request.data['username']
    password=request.data['password']
    
    user=authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        
        token,created = Token.objects.get_or_create(user=user)
        
        return Response({
            "message": "User logged in successfully",
            "token": token.key
        })
    else:
        return Response({
            "message": "Invalid credentials"
        })
        
@api_view(['GET'])
def ProtectedView(request):
    if request.user.is_authenticated:
        return Response({
            "message": "You are already authenticated",
            'username':request.user.username,
            'password':request.user.password


                         })
    else:
        return Response({"message": "Please Login"})