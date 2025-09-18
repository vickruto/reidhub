from pydantic import BaseModel, Field
from typing import List, Optional


class Location(BaseModel):
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class DatasetConfig(BaseModel):
    url: List[str]
    size: Optional[int] = None
    images: Optional[int] = None
    species: List[str] = []
    citations: List[str] = []
    readiness_level: Optional[str] = None
    licence: Optional[str] = None
    location: Location = Field(default_factory=Location)
