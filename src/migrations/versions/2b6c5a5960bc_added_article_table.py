"""Added article table

Revision ID: 2b6c5a5960bc
Revises: 
Create Date: 2024-04-08 16:20:16.180995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b6c5a5960bc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('title_kr', sa.String(length=150), nullable=False),
    sa.Column('title_jp', sa.String(length=150), nullable=False),
    sa.Column('content_kr', sa.String(length=3000), nullable=False),
    sa.Column('content_jp', sa.String(length=3000), nullable=False),
    sa.Column('original_article_url', sa.String(length=255), nullable=False),
    sa.Column('thumbnail_url', sa.String(length=255), nullable=True),
    sa.Column('original_language_code', sa.String(length=8), nullable=False),
    sa.Column('preview_content_kr', sa.String(length=100), nullable=False),
    sa.Column('preview_content_jp', sa.String(length=100), nullable=False),
    sa.Column('date', sa.String(length=8), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=False),
    sa.Column('view_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('articles')
    # ### end Alembic commands ###
