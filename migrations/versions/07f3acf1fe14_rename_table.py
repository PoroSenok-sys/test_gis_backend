"""rename table

Revision ID: 07f3acf1fe14
Revises: 73359934cbd9
Create Date: 2024-11-16 11:24:08.240992

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '07f3acf1fe14'
down_revision: Union[str, None] = '73359934cbd9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('circle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('radius', sa.Float(), nullable=False),
    sa.Column('num_points', sa.Integer(), nullable=False),
    sa.Column('geojson', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('circle_cache')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('circle_cache',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('latitude', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('longitude', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('radius', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('num_points', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('geojson', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='circle_cache_pkey')
    )
    op.drop_table('circle')
    # ### end Alembic commands ###
