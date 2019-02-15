from django.shortcuts import render, HttpResponse
from .forms import UserForm
from .models import User, Room
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import UserCreateSerializer, RoomCreateSerializer, UserLoginSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.permissions import AllowAny        

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class RoomCreateAPIView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    serializer_class = RoomCreateSerializer

    def get(self, request, format=None):
        print(request.user)
        room = Room.objects.filter(user=request.user)
        serializer = RoomCreateSerializer(room, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        room = RoomCreateSerializer(data=request.data)
        if room.is_valid():
            room.save()
            return Response(room.data, status=HTTP_201_CREATED)
        return Response(room.errors, status=HTTP_400_BAD_REQUEST)


class UserLoginApiView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializers

    def post(self,request,*args,**kwargs):
        data = request.data
        serializer = UserLoginSerializers(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
