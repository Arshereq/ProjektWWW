from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Osoba.models import Druzyna,Osoba
from Osoba.Serializer import DruzynaSerializer
from rest_framework.views import APIView


class DruzynaList(APIView):
    def get(self, request, format=None):
        snippets = Druzyna.objects.all()
        serializer = DruzynaSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DruzynaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
