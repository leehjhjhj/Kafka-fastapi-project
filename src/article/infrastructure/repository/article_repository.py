from sqlalchemy import select
from article.domain.model import Article

class ArticleRepository:
    def __init__(self, session):
        self._session = session

    async def find_all(self):
        async with self._session as session:
            results = await session.execute(select(Article))
            return results.scalars().all()
        
    async def find_by_id(self, id: int):
        async with self._session as session:
            result = await session.execute(select(Article).where(Article.id==id))
            return result.scalars().first()