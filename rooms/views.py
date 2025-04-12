# 'views' can be changed to any words

from django.shortcuts import render
from django.http import HttpResponse
from .models import Room


# Create your views here.
def see_all_rooms(request):
    rooms = Room.objects.all()
    return HttpResponse(200)


def see_one_rooms(request, room_pk):
    room = Room.objects.get(pk=room_pk)
    return HttpResponse(200)
