
from dataclasses import dataclass


@dataclass
class Post:
    author: str
    content: str
    time: str
    tags: list
