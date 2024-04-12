from config import Base
from sqlalchemy import Column, BigInteger, String, Integer, DateTime

class Article(Base):
    __tablename__ = "articles"

    id = Column(BigInteger, primary_key=True)
    title_kr = Column(String(150), nullable=False)
    title_jp = Column(String(150), nullable=False)
    content_kr = Column(String(3000), nullable=False)
    content_jp = Column(String(3000), nullable=False)
    original_article_url = Column(String(255), nullable=False)
    thumbnail_url = Column(String(255), nullable=True)
    preview_content_kr = Column(String(100), nullable=False)
    preview_content_jp = Column(String(100), nullable=False)
    date = Column(String(30), nullable=False)
    create_at = Column(DateTime, nullable=False)
    original_language_code = Column(String(8), nullable=False)
    source_newspaper = Column(String(50), nullable=False)
    view_count = Column(Integer, default=0)