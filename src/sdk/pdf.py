"""
pdf automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .pdf_external import PDFExternal
from .pdf_file import PDFFile
from .rich_text import RichText


class PDF(BaseModel):
    caption: Optional[List[RichText]] = Field(default=None, alias="caption")
    type: Optional[str] = Field(default=None, alias="type")
    pass


