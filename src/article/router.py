from fastapi import APIRouter, HTTPException
from article.infrastructure.schemas.article import ArticleListResponse, ArticleDetailResponse
from .container import ArticleContainer

article_router = APIRouter()

@article_router.get('/', response_model=list[ArticleListResponse])
async def list(
    language: str = 'kr'
):
    try:
        article_service = ArticleContainer.article_service()
        article_list_response = await article_service.get_article_list(language)
        return article_list_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@article_router.get('/{article_id}', response_model=ArticleDetailResponse)
async def detail(
    article_id: int,
    language: str = 'kr'
):
    try:
        article_service = ArticleContainer.article_service()
        article_detail_response = await article_service.get_article_detail(article_id, language)
        return article_detail_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))