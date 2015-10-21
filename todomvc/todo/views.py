from django.shortcuts import render
from rest_framework import viewsets
from .models import ToDo
from .serializers import *
from rest_framework.views import APIView

# Create your views here.


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    # def list(self, request):
    #     serializer = ToDoSerializer(queryset, many=True)
    #     return Response(serializer.data)
