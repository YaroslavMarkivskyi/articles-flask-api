from sqlalchemy import MetaData
from sqlalchemy.orm import as_declarative, declared_attr


@as_declarative(metadata=MetaData())
class BaseModel:
    """
    Base model for all models.
    """

    @classmethod
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + str("s")