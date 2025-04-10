from os import name
from rest_framework.decorators import api_view
from rest_framework.response import Response    
from .models import *
from rest_framework import serializers


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookmodel  # Ensure correct capitalization
        fields = '__all__'  # Fix typo from 'feilds' to 'fields'

    def validate(self, data):
        price = data['price']
        if price < 0:
            raise serializers.ValidationError("Price cannot be negative")
        return data



# @api_view(['GET'])
# def booklistapi(request):
#     #Fetch from database and we send response
#     books =bookmodel.objects.all()
#     serializers=BookModelSerializer(books,many=True)
    

#     # books =[{
#     #     'id':books.id,
#     #     'name':books.name,
#     #     'author':books.author,
#     #     'price':books.price
#     # } for books in books]

#     return Response(serializers.data)

# @api_view(['POST'])
# def bookcreateapi(request):
    
#     data=request.data
#     serializers=BookModelSerializer(data=data)
    
#     if serializers.is_valid():
#         serializers.save()
#     # name = data.get('name')
#     # author = data.get('author')
#     # price = data.get('price')

#     # bookmodel(name=name, author=author, price=price).save()
#         return Response({
#             "message":"Book created successfully"
#         })
#     return Response(serializers.errors)

# @api_view(['PUT'])
# def bookupdateapi(request, id):
#     data=request.data

#     book=bookmodel.objects.get(id=id)
#     serializers=BookModelSerializer(instance=book,data=data)
#     # book.name=data['name']
#     # book.author=data['author']
#     # book.price=data['price']

#     # book.save()
#     if serializers.is_valid():
#         serializers.save()
        
#         return Response({
#         "message":"Book updated successfully"
#         })
#     return Response(serializers.errors)

# @api_view(['DELETE'])
# def bookdeleteapi(request, id):
#     data=request.data
#     book=bookmodel.objects.get(id=id)
#     book.delete()
#     return Response({
#         "message":"Book deleted successfully"
#     })


from rest_framework.viewsets import ModelViewSet

class BookViewSet(ModelViewSet):
    queryset =bookmodel.objects.all()
    serializer_class=BookModelSerializer
    
    