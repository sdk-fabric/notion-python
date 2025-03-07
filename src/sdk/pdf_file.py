"""
pdf_file automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .pdf import PDF
from .file_object import FileObject


class PDFFile(PDF):
    file: Optional[FileObject] = Field(default=None, alias="file")
    pass


