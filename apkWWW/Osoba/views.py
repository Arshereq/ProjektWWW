from django.shortcuts import render
from .models import Osoba
from Osoba.Serializer import OsobaSerializer
from rest_framework import status, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .permission import IsOwnerOrReadOnly


@api_view(['GET','POST'])
def osoba_list(request):
    if request.method == 'GET':
        osoba = Osoba.objects.all()
        serializer = OsobaSerializer(osoba, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def osoba_detail(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        osoba = Osoba.objects.get(pk=pk)
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def osoba_create(request):
    if request.method == 'POST':
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsOwnerOrReadOnly])
def osoba_delete(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        person = Osoba.objects.get(pk=pk)
        serializer = OsobaSerializer(person)
        return Response(serializer.data)
    if request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def osoba_list(request):
#     if request.method == 'GET':
#         persons = Osoba.objects.all()
#         serializer = OsobaSerializer(persons, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = OsobaSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def osoba_detail(request, pk):
#     try:
#         person = Osoba.objects.get(pk=pk)
#     except Osoba.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         person = Osoba.objects.get(pk=pk)
#         serializer = OsobaSerializer(person)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = OsobaSerializer(person, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         person.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
