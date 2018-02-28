from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.
class HelloApiView(APIView):
    """Rest API View example"""
    
    serializers_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions(get, post, delete, put)',
            'It is similar to a traditional Django view',
            'Gives you the most control over the logic',
            'It Mapped manually to URLS'
        ]
        return Response({'message':'Hello!', 'an_apiview':an_apiview})
    
    def post(self, request):
        """ Create a hello message with passed name """
        
        serializer = serializers.HelloSerializer(data = request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        """ put method"""
        
        return Response({'method':'Put'})
    
    def patch(self, request, pk=None):
        """ patch request. partially updating the object"""
        
        return Response({'method':'patch'})
    
    def delete(self, request, pk=None):
        """ delete object"""
        
        return Response({'method':'delete'})
    
class HelloViewSet(viewsets.ViewSet):
    """ ViewSets example"""
    
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        """ provide list viewsets"""
        a_view = [
            'Uses actions',
            'Automatically maps to urls routers',
            'provide more functionalioty with less code'
        ]
        
        return Response({'message':'Hello!', 'a_view':a_view})
    
    def create(self, request):
        """ create a new hello message"""
        serializer = serializers.HelloSerializer(data = request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)
            return Response({'message':message})
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrive(self, request, pk=None):
        """ handles getting an object by ID"""
        return Response({'http_method':"GET"})
    