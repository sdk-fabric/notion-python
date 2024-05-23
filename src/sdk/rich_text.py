"""
rich_text automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
from .rich_text_annotation import RichTextAnnotation
class RichText(BaseModel):
    type: Optional[str] = Field(default=None, alias="type")
    annotations: Optional[RichTextAnnotation] = Field(default=None, alias="annotations")
    plain_text: Optional[str] = Field(default=None, alias="plain_text")
    href: Optional[str] = Field(default=None, alias="href")
    pass
