from django.shortcuts import render
from django.http import Http404
from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status


# Create your views here.
class SongList(APIView):

    def get(self, request):
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SongDetail(APIView):

    def get_object(self, pk):
        try:
            return Song.objects.get(id=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        song = self.get_object(pk)
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        song = self.get_object(pk)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        song = self.get_object(pk)
        serializer = SongSerializer(song)
        song.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)


class LikeSong(APIView):

    def get_object(self, pk):
        try:
            return Song.objects.get(id=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        song = self.get_object(pk)
        song.likes += 1
        song.save()
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UnlikeSong(APIView):

    def get_object(self, pk):
        try:
            return Song.objects.get(id=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        song = self.get_object(pk)
        song.likes -= 1
        song.save()
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)
