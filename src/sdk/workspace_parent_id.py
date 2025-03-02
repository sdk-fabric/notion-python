"""
workspace_parent_id automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .parent_id import ParentId


class WorkspaceParentId(ParentId):
    workspace: Optional[bool] = Field(default=None, alias="workspace")
    pass


