from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Rest API View example"""
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions(get, post, delete, put)',
            'It is similar to a traditional Django view',
            'Gives you the most control over the logic',
            'It Mapped manually to URLS'
        ]
        return Response({'message':'Hello!', 'an_apiview':an_apiview})
    