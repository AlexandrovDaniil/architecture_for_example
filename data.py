from dataclasses import dataclass
from datetime import datetime
from typing import TypedDict


@dataclass
class User:
    id: int
    name: str
    surname: str

@dataclass
class Book:
    id: int
    title: str
    author: str
    status: bool

@dataclass
class UserBook:
    user_id: int
    book_id: int

@dataclass
class Note:
    id: int
    name: str
    author: str
    number_of_likes: int


@dataclass
class Issue:
    id: int
    title: str
    author: str
    executor: str
    tags: list
    date_of_create: datetime
    date_of_update: datetime
# support both positional and keyword args
# itemdto1 = ItemDto(
#     name="Old Rod",
#     location="eqrer",
#     description="Fish for low-level Pokemon",
# )
# print(itemdto1)
