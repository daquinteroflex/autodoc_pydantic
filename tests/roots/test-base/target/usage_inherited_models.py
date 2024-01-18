from pydantic import BaseModel
from abc import ABC

__all__ = ["ChildModel", "MultiParentChildModel", "ParentModel"]


class ParentModel(BaseModel):
    """Base class."""

    field_0: int = 10
    """Base field."""


class ChildModel(ParentModel):
    """Nested model."""

    field_1: int = 10
    """Nested field."""


class MultiParentChildModel(ChildModel, ABC):
    """Nested model."""

    field_2: int = 10
    """Double Nested field."""

class GrandChildModel(MultiParentChildModel):
    """Nested model."""

    field_2: int = 10
    """Double Nested field."""

