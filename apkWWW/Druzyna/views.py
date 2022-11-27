from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

from Osoba.models import Druzyna,Osoba
from Osoba.Serializer import DruzynaSerializer, OsobaSerializer


@api_view(['GET'])
def druzyna_list(request):
    if request.method == 'GET':
        druzyna = Druzyna.objects.all()
        serializer = DruzynaSerializer(druzyna, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def druzyna_detail(request, pk):
    try:
        druzyna = Druzyna.objects.get(pk=pk)
    except Druzyna.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        druzyna = Druzyna.objects.get(pk=pk)
        serializer = DruzynaSerializer(druzyna)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def Druzyna_update_delete_add(request, pk):
    try:
        druzyna = Druzyna.objects.all(pk=pk)
    except Druzyna.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = DruzynaSerializer(druzyna, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        druzyna.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        serializer = DruzynaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class DruzynaIdOsoba(APIView):
    def get(self,request,pk,format=None):
        osoba=Osoba.objects.filter(druzyna_id=pk)
        serializer = OsobaSerializer(osoba, many=True)
        return Response(serializer.data)

# @api_view(['GET','POST'])
# def druzyna_list(request):
#     if request.method == 'GET':
#         team = Druzyna.objects.all()
#         serializer = DruzynaSerializer(team, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = DruzynaSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def druzyna_detail(request, pk):
#     try:
#         team = Druzyna.objects.get(pk=pk)
#     except Druzyna.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         team = Druzyna.objects.get(pk=pk)
#         serializer = DruzynaSerializer(team)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = DruzynaSerializer(team, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         team.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
