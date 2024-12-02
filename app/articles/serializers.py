from dataclasses import dataclass
from typing import Optional


@dataclass
class ArticleSerializer:
    id: Optional[int]
    author_id: int
    title: str
    description: str
    body: str

    @staticmethod
    def from_dict(data: dict) -> "ArticleSerializer":
        return ArticleSerializer(
            id=data.get("id"),
            author_id=data["author_id"],
            title=data["title"],
            description=data["description"],
            body=data["body"],
        )


    def to_dict(self):
        return {
            "id": self.id,
            "author_id": self.author_id,
            "title": self.title,
            "description": self.description,
            "body": self.body
        }
