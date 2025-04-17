from unicodedata import category
from .models import Room, Amenity
from django.db import transaction
from categories.models import Category
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
    ValidationError,
)
from .serializers import AmenitySerializer, RoomListSerializer, RoomDetailSerializer

# * 'views'.py can be changed to any words


class Amenities(APIView):

    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(
            all_amenities,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            new_amenity = serializer.save()
            return Response(AmenitySerializer(new_amenity).data)
        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):

    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        # * add ***DoesNotExist***
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(
            amenity,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_amenity = serializer.save()
            return Response(AmenitySerializer(updated_amenity).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )


class Rooms(APIView):
    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(
            all_rooms,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_authenticated:
            # print(request.data)
            serializer = RoomDetailSerializer(data=request.data)
            if serializer.is_valid():
                category_pk = request.data.get("category")
                if not category_pk:
                    raise ParseError("Category is required.")
                try:
                    category = Category.objects.get(pk=category_pk)
                    if category.kind == Category.CategoryKindCoices.EXPERIENCES:
                        raise ParseError("The category kind should be 'rooms'.")
                except Category.DoesNotExist:
                    raise ParseError("Category not found.")
                try:
                    # Transaction - not commit change immediately, prevent create too many pk
                    with transaction.atomic():
                        # foreign key handling
                        room = serializer.save(
                            owner=request.user,
                            category=category,
                        )
                        # many to many fields handling
                        amenities = request.data.get("amenities")
                        for amenity_pk in amenities:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                            room.amenities.add(amenity)
                except Exception:
                    raise ParseError("Amenity not found.")

                serializer = RoomDetailSerializer(room)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class RoomDetail(APIView):

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomDetailSerializer(room)
        return Response(serializer.data)

    def put(self, request, pk):
        room = self.get_object(pk)
        # user authentication
        if not request.user.is_authenticated:
            raise NotAuthenticated
        # check user is owner of the room
        if request.user != room.owner:
            raise PermissionDenied
        serializer = RoomDetailSerializer(
            room,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            if request.data.get("category"):
                try:
                    category_pk = request.data.get("category")
                    print(category_pk)
                    category = Category.objects.get(pk=category_pk)
                    if category.kind == Category.CategoryKindCoices.EXPERIENCES:
                        raise ParseError("The category kind should be 'rooms'.")
                except Category.DoesNotExist:
                    raise ParseError("Category Not Found")
            else:
                category = room.category
            try:
                with transaction.atomic():
                    serializer.save(owner=request.user, category=category)
                    if request.data.get("amenities"):
                        amenities = request.data.get("amenities")
                        room.amenities.clear()
                        # print(amenities)
                        for amenity_pk in amenities:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                            room.amenities.add(amenity)
                    return Response(serializer.data)
            except Exception:
                raise ValidationError

    def delete(self, request, pk):
        room = self.get_object(pk)
        # print(dir(request.user))
        # user authentication
        if not request.user.is_authenticated:
            raise NotAuthenticated
        # check user is owner of the room
        if request.user != room.owner:
            raise PermissionDenied
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)
