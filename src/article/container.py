from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import async_scoped_session, create_async_engine, async_sessionmaker
from core.config import get_async_mysql_uri
import asyncio
from common.infrastructure.uow import UnitOfWork
from article.infrastructure.repository.article_repository import ArticleRepository
from article.service.article_service import ArticleService

class ArticleContainer(containers.DeclarativeContainer):
    engine = create_async_engine(get_async_mysql_uri(), echo=True)
    session_factory = async_sessionmaker(bind=engine)
    session = providers.Factory(
        async_scoped_session,
        session_factory=session_factory,
        scopefunc=asyncio.current_task
    )
    article_unit_of_work = providers.Factory(
        UnitOfWork,
        session=session,
        repository_cls=ArticleRepository
    )
    article_service = providers.Factory(
        ArticleService,
        article_unit_of_work
    )