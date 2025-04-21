import strawberry
import typing

import strawberry.django
from . import types
from . import queries


@strawberry.type
class Query:
    all_rooms: typing.List[types.RoomType] = strawberry.field(
        resolver=queries.get_all_rooms
    )
    # nullable
    room: typing.Optional[types.RoomType] = strawberry.field(resolver=queries.get_room)
