"""
database_title automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .database_annotations import DatabaseAnnotations


class DatabaseTitle(BaseModel):
    type: Optional[str] = Field(default=None, alias="type")
    text: Optional[str] = Field(default=None, alias="text")
    annotations: Optional[DatabaseAnnotations] = Field(default=None, alias="annotations")
    plain_text: Optional[str] = Field(default=None, alias="plain_text")
    href: Optional[str] = Field(default=None, alias="href")
    pass


