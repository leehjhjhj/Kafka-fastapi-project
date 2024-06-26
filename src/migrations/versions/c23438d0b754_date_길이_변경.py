"""date 길이 변경

Revision ID: c23438d0b754
Revises: e7aa7c867bfc
Create Date: 2024-04-12 14:35:47.136808

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'c23438d0b754'
down_revision: Union[str, None] = 'e7aa7c867bfc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('articles', 'date',
               existing_type=mysql.VARCHAR(length=8),
               type_=sa.String(length=30),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('articles', 'date',
               existing_type=sa.String(length=30),
               type_=mysql.VARCHAR(length=8),
               existing_nullable=False)
    # ### end Alembic commands ###
