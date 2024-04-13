from pydantic import BaseModel, Field
from typing import Optional

class ArticleListResponse(BaseModel):
    id : int
    title : str = Field(..., serialization_alias='title')
    preview_content : str = Field(..., serialization_alias='previewContent')
    date : str
    thumbnail_url : Optional[str] = Field(..., serialization_alias='thumbnailUrl')
    view_count: int = Field(..., serialization_alias='viewCount')