from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from falabella.quickstart.serializers import UserSerializer, GroupSerializer
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


def GetVenta(request):
    return JsonResponse({'Código Retornado': '201'}, status=201)
    #return Response(status=status.HTTP_201_CREATED)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



