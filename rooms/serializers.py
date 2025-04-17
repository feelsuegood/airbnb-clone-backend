from rest_framework.serializers import ModelSerializer
from .models import Room, Amenity
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "pk",
            "name",
            "description",
        )


class RoomDetailSerializer(ModelSerializer):

    owner = TinyUserSerializer(
        read_only=True,
    )
    amenities = AmenitySerializer(
        read_only=True,
        many=True,
    )
    category = CategorySerializer(
        read_only=True,
    )

    class Meta:
        model = Room
        fields = "__all__"
        depth = 1

    # * create function automatically called when serializer.save() is called in BTS
    # def create(self, validated_data):
    #     return Room.objects.create(**validated_data)

    # * test code to prevent create a room
    # def create(self, validated_data):
    #     # print(validated_data)
    #     return


class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "city",
            "country",
            "price",
        )
