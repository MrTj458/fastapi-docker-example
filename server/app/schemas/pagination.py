from typing import TypeVar, Generic

from pydantic.generics import GenericModel

DataT = TypeVar('DataT')

class Page(GenericModel, Generic[DataT]):
    page: int
    total_pages: int
    data: DataT
