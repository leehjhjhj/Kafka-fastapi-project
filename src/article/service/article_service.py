from config import AsyncSession
from article.domain.model import Article
from sqlalchemy import select
from article.infrastructure.schemas.article import ArticleListResponse

class ArticleService:
    async def get_article_list(self, language: str):
        async with AsyncSession() as session:
            results = await session.execute(select(Article))
            articles = results.scalars().all()
            articles = [self._convert_article(article=article, language=language) for article in articles]
            return articles
            
    def _convert_article(self, article: Article, language: str):
        title = article.title_jp if language == 'jp' else article.title_kr
        preview_content = article.preview_content_jp if language == 'jp' else article.preview_content_kr
        return ArticleListResponse(
            id=article.id,
            title=title,
            preview_content=preview_content,
            date=article.date,
            thumbnail_url=article.thumbnail_url,
            view_count=article.view_count
        )