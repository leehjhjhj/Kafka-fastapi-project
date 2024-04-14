from article.domain.model import Article
from article.infrastructure.schemas.article import ArticleListResponse, ArticleDetailResponse
from common.infrastructure.uow import UnitOfWork

class ArticleService:
    def __init__(self, uof: UnitOfWork):
        self._uof = uof

    async def get_article_list(self, language: str):
        async with self._uof:
            articles = await self._uof.repo.find_all()
            response_articles = [self._convert_list_article(article=article, language=language) for article in articles]
            return response_articles
    
    async def get_article_detail(self, article_id: int, language: str,):
        async with self._uof:
            article = await self._uof.repo.find_by_id(id=article_id)
            return self._convert_detail_article(article, language)

    def _convert_list_article(self, article: Article, language: str):
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
    
    def _convert_detail_article(self, article: Article, language: str):
        title = article.title_jp if language == 'jp' else article.title_kr
        content = article.content_jp if language == 'jp' else article.content_kr
        return ArticleDetailResponse(
            id=article.id,
            title=title,
            content=content,
            date=article.date,
            view_count=article.view_count,
            original_article_url=article.original_article_url
        )