from config import settings
import strawberry
import strawberry.django
import typing
from strawberry import auto
from reviews.types import ReviewType
from . import models
from users.types import UserType


@strawberry.django.type(models.Room)
class RoomType:
    pk: auto = strawberry.django.field(field_name="id")
    name: auto
    kind: auto
    owner: "UserType"

    @strawberry.field
    def reviews(self, page: typing.Optional[int] = 1) -> typing.List["ReviewType"]:
        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size
        return self.reviews.all()[start:end]

    @strawberry.field
    def rating(self) -> str:
        return self.rating()
