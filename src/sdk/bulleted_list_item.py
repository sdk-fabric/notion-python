"""
bulleted_list_item automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .bulleted_list_item import BulletedListItem
from .block import Block


class BulletedListItem(BaseModel):
    rich_text: Optional[List[BulletedListItem]] = Field(default=None, alias="rich_text")
    color: Optional[str] = Field(default=None, alias="color")
    children: Optional[List[Block]] = Field(default=None, alias="children")
    pass


