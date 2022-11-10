from django.shortcuts import render
from rest_framework.views import APIView

from .models import Osoba
from Osoba.Serializer import OsobaSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class OsobaList(APIView):
    def get(self, request, format=None):
        snippets = Osoba.objects.all()
        serializer = OsobaSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
