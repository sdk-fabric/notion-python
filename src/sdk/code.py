"""
code automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .rich_text import RichText


class Code(BaseModel):
    caption: Optional[List[RichText]] = Field(default=None, alias="caption")
    rich_text: Optional[List[RichText]] = Field(default=None, alias="rich_text")
    language: Optional[str] = Field(default=None, alias="language")
    pass


