"""
block_heading_2 automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .block import Block
from .block_heading_2 import BlockHeading


class BlockHeading(Block):
    heading__: Optional[BlockHeading] = Field(default=None, alias="heading_2")
    pass


