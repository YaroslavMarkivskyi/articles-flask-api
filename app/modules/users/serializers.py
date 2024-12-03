from dataclasses import dataclass
from typing import Optional


@dataclass
class UserSerializer:
    id: Optional[int]
    username: str
    email: str
    role: str
    password: str

    @staticmethod
    def from_dict(data: dict) -> "UserSerializer":
        """Створює екземпляр UserSerializer із словника."""
        return UserSerializer(
            id=data.get("id"),
            username=data["username"],
            email=data["email"],
            role=data["role"],
            password=data["password"],  # Передбачається, що пароль уже захешовано
        )

    def to_dict(self):
        """Конвертує екземпляр UserSerializer у словник."""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "password": self.password,  # У продакшені пароль зазвичай не повертається
        }
