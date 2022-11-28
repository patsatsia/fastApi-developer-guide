from fastapi import HTTPException
from pydantic import BaseModel, Field, ValidationError
from starlette import status

from src.config import settings


class PaginationParamsSchema(BaseModel):
    page: int = Field(ge=1)
    limit: int = Field(ge=0)


class PaginationQueryParams:
    def __init__(self, page: int = 1, limit: int = settings.PAGE_SIZE):
        self._validate_query_params(page=page, limit=limit)
        self.page = page
        self.limit = limit
        self.offset = self.limit * (page - 1)

    @staticmethod
    def _validate_query_params(**kwargs):
        try:
            return PaginationParamsSchema(**kwargs)
        except ValidationError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.errors())
