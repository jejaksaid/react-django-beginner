from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room


# Create your views here.
class RooView(generics.CreateAPIView):
    queryset = Room.object.all()
    serializer_class = RoomSerializer